import csv

def initialize_csv(file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Track ID", "Entry Time", "Exit Time", "Time Spent (seconds)"])

def log_to_csv(file_path, data):
    try:
        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
    except Exception as e:
        print(f"Error writing to CSV: {e}")