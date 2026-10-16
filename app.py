from __future__ import annotations

import os
import json
import threading
import time
from pathlib import Path

import cv2
import numpy as np
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from starlette.concurrency import run_in_threadpool
from ultralytics import YOLO


ROOT = Path(__file__).resolve().parent
WEB_APP = ROOT / "static" / "index.html"
MODEL_SPEC = os.getenv("YOLO_MODEL", "yolo26n.pt")
MODEL: YOLO | None = None
MODEL_LOCK = threading.Lock()

app = FastAPI(title="AeroSight", version="1.0.0")


def get_model() -> YOLO:
    global MODEL
    if MODEL is None:
        with MODEL_LOCK:
            if MODEL is None:
                MODEL = YOLO(MODEL_SPEC)
    return MODEL


def model_labels(model: YOLO) -> dict[int, str]:
    names = model.names
    if isinstance(names, list):
        return {index: str(label) for index, label in enumerate(names)}
    return {int(index): str(label) for index, label in names.items()}


def infer_jpeg(payload: bytes, confidence: float) -> dict[str, object]:
    encoded = np.frombuffer(payload, dtype=np.uint8)
    frame = cv2.imdecode(encoded, cv2.IMREAD_COLOR)
    if frame is None:
        raise ValueError("The received frame could not be decoded.")

    model = get_model()
    start = time.perf_counter()
    with MODEL_LOCK:
        prediction = model.predict(frame, conf=confidence, verbose=False)[0]
    elapsed_ms = (time.perf_counter() - start) * 1000
    height, width = frame.shape[:2]
    labels = model_labels(model)
    person_ids = {
        label_id
        for label_id, label in labels.items()
        if label.strip().casefold() in {"person", "people", "human", "0"}
    }
    boxes = []

    if prediction.boxes is not None:
        for box in prediction.boxes:
            class_id = int(box.cls.item())
            if person_ids and class_id not in person_ids:
                continue
            x1, y1, x2, y2 = (float(value) for value in box.xyxy[0].tolist())
            boxes.append(
                {
                    "x": max(0.0, min(1.0, x1 / width)),
                    "y": max(0.0, min(1.0, y1 / height)),
                    "w": max(0.0, min(1.0, (x2 - x1) / width)),
                    "h": max(0.0, min(1.0, (y2 - y1) / height)),
                    "confidence": float(box.conf.item()),
                    "label": labels.get(class_id, str(class_id)),
                }
            )

    return {
        "type": "result",
        "boxes": boxes,
        "count": len(boxes),
        "inference_ms": round(elapsed_ms, 1),
        "width": width,
        "height": height,
    }


@app.get("/")
def home() -> FileResponse:
    return FileResponse(WEB_APP)


@app.get("/api/health")
def health() -> dict[str, object]:
    return {
        "status": "ok",
        "app": "AeroSight",
        "model": MODEL_SPEC,
        "model_loaded": MODEL is not None,
        "roboflow_required": False,
    }


@app.websocket("/ws/infer")
async def infer_socket(websocket: WebSocket) -> None:
    await websocket.accept()
    try:
        settings = await websocket.receive_json()
        confidence = float(settings.get("confidence", 0.35))
        if not 0.01 <= confidence <= 0.99:
            await websocket.send_json({"type": "error", "message": "Confidence must be between 0.01 and 0.99."})
            await websocket.close(code=1008)
            return

        model = await run_in_threadpool(get_model)
        await websocket.send_json(
            {"type": "ready", "model": MODEL_SPEC, "labels": model_labels(model)}
        )

        while True:
            message = await websocket.receive()
            payload = message.get("bytes")
            if payload is None:
                text = message.get("text")
                if text == "stop":
                    break
                if text:
                    try:
                        updated = json.loads(text)
                        updated_confidence = float(updated.get("confidence", confidence))
                    except (TypeError, ValueError, json.JSONDecodeError):
                        await websocket.send_json({"type": "error", "message": "Settings must contain a numeric confidence value."})
                        continue
                    if not 0.01 <= updated_confidence <= 0.99:
                        await websocket.send_json({"type": "error", "message": "Confidence must be between 0.01 and 0.99."})
                        continue
                    confidence = updated_confidence
                continue
            if len(payload) > 4_000_000:
                await websocket.send_json({"type": "error", "message": "Frame is too large; lower the video resolution."})
                continue
            try:
                result = await run_in_threadpool(infer_jpeg, payload, confidence)
                await websocket.send_json(result)
            except ValueError as error:
                await websocket.send_json({"type": "error", "message": str(error)})
    except WebSocketDisconnect:
        return
    except Exception as error:  # send a useful local diagnostic without terminating the app
        try:
            await websocket.send_json({"type": "error", "message": f"Inference failed: {error}"})
        except Exception:
            pass
    finally:
        if websocket.client_state.name == "CONNECTED":
            await websocket.close()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="127.0.0.1", port=int(os.getenv("PORT", "8000")), reload=False)
