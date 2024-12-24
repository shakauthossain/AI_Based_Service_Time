import cv2

def define_zones(frame):
    zones = []
    drawing = False
    temp_zone = None

    def draw_rectangle(event, x, y, flags, param):
        nonlocal drawing, temp_zone

        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            temp_zone = [(x, y)]  # Start of the rectangle
        elif event == cv2.EVENT_MOUSEMOVE and drawing:
            temp_zone[1:] = [(x, y)]  # Update the end of the rectangle as the mouse moves
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            temp_zone.append((x, y))  # Finalize the zone
            zones.append(tuple(temp_zone))  # Add zone as a tuple (start, end)

    # Open the window to define zones
    cv2.namedWindow("Define Zones")
    cv2.setMouseCallback("Define Zones", draw_rectangle)

    while True:
        temp_frame = frame.copy()

        # Draw all the defined zones on the frame
        for zone in zones:
            cv2.rectangle(temp_frame, zone[0], zone[1], (0, 255, 0), 2)  # Green zones

        # Draw the current zone being defined
        if temp_zone:
            cv2.rectangle(temp_frame, temp_zone[0], temp_zone[-1], (255, 0, 0), 2)  # Blue rectangle for the current zone

        # Display the frame with zones
        cv2.imshow("Define Zones", temp_frame)

        # Wait for key press to finalize
        key = cv2.waitKey(1) & 0xFF
        if key == ord('r'):  # Press 'r' to finish defining zones
            break

    cv2.destroyWindow("Define Zones")
    return zones