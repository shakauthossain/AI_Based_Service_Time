import cv2
import csv
from zone_selector import define_zones
from human_detector import detect_and_track, display_logs
from utilities import initialize_csv
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

def main(video_path=None):
    # Define the CSV file for logging
    csv_file = "Service_Time.csv"
    initialize_csv(csv_file)

    # Initialize YOLO model and DeepSORT tracker
    model = YOLO('yolov8n.pt')
    tracker = DeepSort(max_age=50, n_init=3)

    # Open video source
    if video_path:
        cap = cv2.VideoCapture(video_path)
    else:
        cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Read the first frame to define zones
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read video.")
        return

    # Define zones interactively
    zones = define_zones(frame)
    print("Zones defined:", zones)

    # Initialize logs
    time_logs = []

    # Process video frame by frame
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Draw zones on the frame
        for zone in zones:
            cv2.rectangle(frame, zone[0], zone[1], (0, 0, 255), 2)  # Green zone rectangles

        # Detect and track humans
        output_frame = detect_and_track(frame, model, tracker, zones, time_logs, csv_file)

        # Display logs on the frame
        display_logs(output_frame, time_logs)

        # Show the processed frame
        cv2.imshow("Human Detection and Zone Timing", output_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = 'fringestorez.mp4'  # Replace with the actual video path or leave None for webcam
    main(video_path)