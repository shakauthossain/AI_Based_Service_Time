# Human Detection and Tracking with Service Time Calculation

This project utilizes computer vision techniques to detect and track humans in a video stream. It calculates the time spent by each detected individual inside a predefined zone and logs the data in a CSV file. The system also calculates the average time spent by each individual and the total average time spent by all detected individuals.

---

## Overview

The goal of this project is to detect and track humans in a video feed and calculate their service time within a specified zone. The system outputs the following information in a CSV file:

- **Track ID**: Unique identifier for each detected individual.
- **Entry Time**: Time when the individual entered the zone.
- **Exit Time**: Time when the individual exited the zone.
- **Time Spent (seconds)**: Duration the individual spent inside the zone.
- **Individual Avg**: The average time spent by the individual inside the zone.
- **Total Avg**: The total average time spent by all detected individuals.

---

## Features

- Detects humans in a video using a YOLO model.
- Dynamically marks zones for tracking using mouse input.
- Tracks the time individuals spend inside the marked zone.
- Logs detailed information, including individual and overall average times, in a CSV file.
- Displays real-time tracking with annotated information on the video.

---

## Prerequisites

To run this project, you need the following Python packages:

- `opencv-python` for computer vision tasks.
- `ultralytics` for YOLO model inference.
- `scikit-learn` for object tracking.
- `csv` and `os` for file handling.
- `time` for time tracking.

Install these dependencies using pip:

```bash
pip install opencv-python ultralytics scikit-learn
```

---

## Setting Up the Zone

### Marking the Zone:
1. **Mouse Input**: Use the mouse to click and drag a rectangle on the video frame to define the zone.
2. **Press "r" to Confirm**: After marking the zone, press "r" to set it.
3. **Press "q" to Quit**: Exit the video either after marking or during tracking.

---

## Usage

### 1. Clone or Download the Repository
Download or clone this repository to your local machine:

```bash
git clone https://github.com/shakauthossain/AI_Based_Service_Time_Tracker.git
cd AI_Based_Service_Time_Tracker
```

### 2. Prepare the Model and Video
- **Model**: Ensure the YOLO model weights are downloaded and placed in the appropriate directory.
- **Video**: Place your video file in the root directory and update the video path in the script:

```python
video_path = "input_video.mp4"  # Replace with your video file path
```

### 3. Run the Script
Run the main Python script:

```bash
python main.py
```

### 4. Output Files
- A CSV file (`time_logs.csv`) is generated in the root directory, containing detailed service time logs.
- Each row includes:

| Track ID | Entry Time         | Exit Time          | Time Spent (seconds) | Individual Avg | Total Avg  |
|----------|--------------------|--------------------|-----------------------|----------------|------------|
| 2        | 1734124712.97      | 1734124720.91      | 7.93                  | 7.93           | 7.93       |

---

## Script Overview

### Detect and Track
The `detect_and_track` function uses YOLO for detection and tracks individuals across frames. It logs their entry and exit times when they move in and out of the marked zone.

### Zone Marking
Zones can be dynamically marked using mouse input. The `run_video_with_zone_marking` function enables this feature, allowing you to interactively define zones during runtime.

### CSV Logging
The `log_to_csv` function saves tracking information to the CSV file in the specified format.

---

## Customization

- **Video Path**: Update `video_path` in the script to the location of your video file.
- **Zone Marking**: Mark zones dynamically by clicking and dragging on the video. Press **"r"** to confirm the zone.
- **Output CSV**: Modify `csv_file` to change the name or location of the generated CSV file.

---

## Troubleshooting

### Detection or Tracking Issues
- Ensure the YOLO model weights are correctly loaded.
- Adjust detection confidence thresholds or retrain the model for better results.

### Zone Setup
If the system doesn’t detect individuals in the zone:
- Ensure the zone is marked correctly.
- Use a video with clear visibility.

### Performance
For longer videos or higher resolutions:
- Optimize the code by resizing frames or limiting detection frequency.

---

## Contact
For questions or suggestions, contact **Shakaut Hossain** at [shakauthossain0@gmail.com](mailto:shakauthossain0@gmail.com).
