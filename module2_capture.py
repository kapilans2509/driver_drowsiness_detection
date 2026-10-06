import cv2
from collections import deque
from module1_config import CLIP_LENGTH

class VideoCaptureModule:
    def __init__(self, camera_index=0):
        self.cap = cv2.VideoCapture(camera_index)
        self.frames = deque(maxlen=CLIP_LENGTH)

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def update_clip(self, frame):
        self.frames.append(frame)

    def get_clip(self):
        if len(self.frames) == CLIP_LENGTH:
            return list(self.frames)
        return None

    def release(self):
        self.cap.release()
