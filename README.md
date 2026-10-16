# AeroSight

Local aerial person detection for video files and live cameras. AeroSight does not call Roboflow or upload video frames: the browser sends frames to a server running on `127.0.0.1`, where a local YOLO model processes them.

## Features

- Process a local MP4, MOV, or WebM file in the browser.
- Run live detection from a connected webcam.
- Adjust confidence and inference frame rate.
- Use a local fine-tuned model by setting `YOLO_MODEL`.
- Keep inference and source video on the local computer.

## Run locally

Use Python 3.10 or newer. Install the packages and start the app:

```powershell
python -m pip install -r requirements.txt
python app.py
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000). The first run downloads the small Ultralytics YOLO26n COCO model if it is not cached. After that, the downloaded model runs locally. An internet connection is needed for this initial setup unless you provide the weights ahead of time.

For a fine-tuned aerial detector, point the app to a compatible local weights file:

```powershell
$env:YOLO_MODEL = 'C:\path\to\best.pt'
python app.py
```

The current default model is a general COCO detector, not the model trained for the Roboflow UAV-Persons-Detection project. Exported fine-tuned weights can be loaded without adding a Roboflow runtime dependency.

## Test a video

Start AeroSight, choose a local video in the interface, and select **Start detection**. Frames are processed locally; the video file is not uploaded or copied into the repository.

## Model and application licensing

The AeroSight application source is MIT licensed. Ultralytics is distributed under AGPL-3.0, and its model weights are separately licensed. Review those terms before redistributing or using the model in a commercial product. Fine-tuned weights may have additional terms from their owner or training platform.
