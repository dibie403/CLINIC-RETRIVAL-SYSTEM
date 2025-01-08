import cv2
import numpy as np
import mediapipe as mp

# Initialize Mediapipe segmentation
mp_selfie_segmentation = mp.solutions.selfie_segmentation
selfie_segmentation = mp_selfie_segmentation.SelfieSegmentation(model_selection=1)

# Read input video
input_path = "Online University.mp4"
output_path = "output_video.webm"

cap = cv2.VideoCapture(input_path)

# Get video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'VP90')  # WebM format with alpha channel
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height), isColor=True)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform segmentation
    results = selfie_segmentation.process(rgb_frame)
    mask = results.segmentation_mask

    # Create transparent background
    background = np.zeros_like(frame)
    mask = np.expand_dims(mask, axis=-1)
    transparent_frame = np.uint8(frame * mask + background * (1 - mask))

    # Write frame to output video
    out.write(transparent_frame)

# Release resources
cap.release()
out.release()
