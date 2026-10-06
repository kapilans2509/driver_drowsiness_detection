import cv2
import torch

from module1_config import LABELS
from module2_capture import VideoCaptureModule
from module3_preprocess import PreprocessModule
from module4_model import Drowsiness3DCNN
from module5_adaptive_logic import AdaptiveLogic
from module6_alerts import AlertModule
from module7_dashboard import DashboardModule
from module8_report import ReportModule

capture = VideoCaptureModule()
preprocess = PreprocessModule()
logic = AdaptiveLogic()
alerts = AlertModule()
dashboard = DashboardModule()
report = ReportModule()

model = Drowsiness3DCNN()
model.load_state_dict(torch.load("best_model.pth", map_location="cpu"))
model.eval()

while True:
    frame = capture.get_frame()

    if frame is None:
        break

    capture.update_clip(frame)
    clip = capture.get_clip()

    label = "Collecting Frames..."

    if clip is not None:
        input_tensor = preprocess.preprocess_clip(clip)
        input_tensor = torch.tensor(input_tensor)

        with torch.no_grad():
            output = model(input_tensor)
            prediction = torch.argmax(output, dim=1).item()

        logic.update_state(prediction)
        label = LABELS[prediction]

        if prediction == 1:
            alerts.mild_alert()
            logic.warning_count += 1

        elif prediction == 2:
            if logic.should_trigger_severe():
                alerts.severe_alert()

                if logic.warning_count >= 2:
                    alerts.voice_alert()

                logic.warning_count += 1

        report.log_event(label, logic.warning_count)

    frame = dashboard.draw_dashboard(
        frame,
        label,
        logic.warning_count,
        logic.consecutive_drowsy
    )

    cv2.imshow("Driver Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
report.save_report()
cv2.destroyAllWindows()
