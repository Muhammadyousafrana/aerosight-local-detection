# AeroSight

![AeroSight local vision pipeline](assets/aerosight-architecture.svg)

**Local video and webcam inference using the trained UAV-Persons-Detection model.** AeroSight loads the project’s YOLOv11n version 3 checkpoint into Ultralytics and processes frames on your computer. The running app does not call Roboflow or upload frames.

## Model provenance

- Roboflow project: `alis-workspace-zktpw/uav-persons-detection`
- Trained model: `uav-persons-detection-3-yolo11n-t1`
- Dataset version: `3`
- Training: YOLOv11n, finished

The checkpoint is not included in Git. Roboflow makes trained-weight downloads available through the model page or Python SDK on eligible plans. Download the version 3 YOLOv11n weights from the [project’s version 3 page](https://app.roboflow.com/alis-workspace-zktpw/uav-persons-detection/3), then place `weights.pt` here:

```text
models/uav-persons-detection-3-yolo11n-t1/weights.pt
```

Roboflow is needed only to obtain the checkpoint. The app has no Roboflow runtime dependency and will report a missing-checkpoint error rather than substitute a generic pretrained model.

## Features

- Detect people in local MP4, MOV, and WebM videos.
- Run live detection from a connected webcam.
- Adjust confidence and inference frame rate in the browser UI.
- Use the project’s trained YOLOv11n version 3 weights by default.
- Keep video frames and inference on the local computer.

## Run locally

Requires Python 3.10 or newer, the local checkpoint above, and the packages in `requirements.txt`.

```powershell
python -m pip install -r requirements.txt
python app.py
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000). If you have another compatible local checkpoint, select it with `YOLO_MODEL`:

```powershell
$env:YOLO_MODEL = 'C:\path\to\weights.pt'
python app.py
```

The app accepts only an existing local weight file; Ultralytics will not fetch a default model from the internet.

## Test a video

Choose a local video or allow webcam access, adjust confidence and frame rate, then select **Start detection**. The video is processed locally and is not copied into the repository. The development test clip came from [Intel's sample videos](https://github.com/intel-iot-devkit/sample-videos); it is not included here.

## Project structure

```text
app.py                              FastAPI server, WebSocket, and local inference
static/index.html                   Browser interface for video and webcam
assets/aerosight-architecture.svg   Local-only architecture illustration
models/.../weights.pt               Locally downloaded project checkpoint (ignored by Git)
```

## Licensing

The AeroSight application source is MIT licensed. Ultralytics is distributed under AGPL-3.0. The trained weights are governed by the Roboflow plan and license terms; confirm that you can use and redistribute them for your intended purpose. The checkpoint is excluded from this repository.
