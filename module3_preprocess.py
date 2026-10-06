import cv2
import numpy as np
from module1_config import FRAME_SIZE

class PreprocessModule:
    def preprocess_clip(self, clip):
        processed = []

        for frame in clip:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            resized = cv2.resize(gray, (FRAME_SIZE, FRAME_SIZE))
            normalized = resized / 255.0
            processed.append(normalized)

        processed = np.array(processed)
        processed = processed.reshape(1, 1, len(processed), FRAME_SIZE, FRAME_SIZE)
        return processed.astype(np.float32)
