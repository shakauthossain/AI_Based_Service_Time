import cv2
import time
from utilities import log_to_csv
import csv
import os



tracked_in_zone = {}

# Global variable to store individual times and counts
individual_times = {}
# Global variables for total time and total entries
total_time_spent = 0
total_entries = 0

def detect_and_track(frame, model, tracker, zones, time_logs, csv_file):
    global total_time_spent, total_entries, individual_times, tracked_in_zone

    results = model(frame)

    detections = []
    for detection in results[0].boxes:
        class_id = int(detection.cls)
        confidence = float(detection.conf)
        if class_id == 0 and confidence >= 0.5:
            x1, y1, x2, y2 = map(int, detection.xyxy[0])
            detections.append(([x1, y1, x2, y2], confidence))

    tracked_objects = tracker.update_tracks(detections, frame=frame)

    for obj in tracked_objects:
        if not obj.is_confirmed():
            continue

        track_id = obj.track_id
        x1, y1, x2, y2 = map(int, obj.to_ltwh())

        inside_zone = any(x1 >= z[0][0] and y1 >= z[0][1] and x2 <= z[1][0] and y2 <= z[1][1] for z in zones)

        if inside_zone:
            if track_id not in tracked_in_zone:
                tracked_in_zone[track_id] = time.time()

            time_spent = time.time() - tracked_in_zone[track_id]
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"ID {track_id}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.putText(frame, f"Time: {time_spent:.1f}s", (x1, y2 + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

        else:
            if track_id in tracked_in_zone:
                exit_time = time.time()
                time_spent = exit_time - tracked_in_zone[track_id]

                # Update the individual times and total times
                if track_id not in individual_times:
                    individual_times[track_id] = {"total_time": 0, "count": 0}
                individual_times[track_id]["total_time"] += time_spent
                individual_times[track_id]["count"] += 1
                individual_avg_time = individual_times[track_id]["total_time"] / individual_times[track_id]["count"]

                # Update total time spent
                total_time_spent += time_spent
                total_entries += 1
                overall_avg_time = total_time_spent / total_entries if total_entries > 0 else 0

                log_to_csv(csv_file, [track_id, tracked_in_zone[track_id], exit_time, time_spent, individual_avg_time, overall_avg_time])

                del tracked_in_zone[track_id]

    return frame




def initialize_csv(csv_file):
    # Check if the file exists or if it is empty
    if not os.path.exists(csv_file) or os.stat(csv_file).st_size == 0:
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Track ID", "Entry Time", "Exit Time", "Time Spent (seconds)", "Individual Avg", "Total Avg"])
            print("CSV initialized with headers.")  # Debugging statement

# Function to log data to CSV
def log_to_csv(csv_file, log_data):
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(log_data)
        print(f"Logged data: {log_data}")  # Debugging statement

# Initialize CSV with headers if needed
csv_file = "Service_Time.csv"
initialize_csv(csv_file)
def display_logs(frame, time_logs):
    y_offset = 30
    for log in time_logs:
        track_id, time_spent = log
        cv2.putText(frame, f"ID {track_id}: {time_spent:.1f}s", (10, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        y_offset += 30