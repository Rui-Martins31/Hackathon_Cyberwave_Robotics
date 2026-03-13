import cv2
import numpy as np
from cyberwave import Cyberwave

from dotenv import load_dotenv
import os

# Constants
load_dotenv()
CYBERWAVE_API_KEY: str = os.getenv("CYBERWAVE_API_KEY")
ASSET_KEY: str         = os.getenv("ASSET_KEY")
TWIN_ID: str           = os.getenv("TWIN_CAMERA_ID")
ENVIRONMENT_ID: str    = os.getenv("ENVIRONMENT_ID")

cw = Cyberwave(api_key=CYBERWAVE_API_KEY)
robot = cw.twin(
    ASSET_KEY,
    twin_id=TWIN_ID,
    environment_id=ENVIRONMENT_ID
)

# ── Single frame as numpy array ───────────────────────────────────────

frame = robot.capture_frame("numpy")  # BGR numpy array

print(f"{frame = }")

# Draw a timestamp overlay
cv2.putText(
    frame,
    "Cyberwave live",
    (10, 30),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (0, 255, 0),
    2,
)

cv2.imwrite("annotated_frame.jpg", frame)
print("Saved annotated_frame.jpg")

# ── Edge detection ────────────────────────────────────────────────────

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)
cv2.imwrite("edges.jpg", edges)
print("Saved edges.jpg")

# ── Batch capture → side-by-side composite ────────────────────────────

frames = robot.capture_frames(3, interval_ms=500, format="numpy")
composite = np.hstack(frames)
cv2.imwrite("composite.jpg", composite)
print(f"Saved composite.jpg ({len(frames)} frames stitched)")

# ── Using the twin.camera namespace ───────────────────────────────────

frame2 = robot.camera.read()  # numpy by default, like cv2.VideoCapture
path = robot.camera.snapshot()  # temp JPEG file
print(f"Snapshot saved to {path}")

# ── PIL example: resize + thumbnail ───────────────────────────────────

pil_frame = robot.capture_frame("pil")
pil_frame.thumbnail((320, 240))
pil_frame.save("thumbnail.jpg")
print("Saved thumbnail.jpg (320x240)")

cw.disconnect()