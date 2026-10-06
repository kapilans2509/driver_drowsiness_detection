import cv2

class DashboardModule:
    def draw_dashboard(self, frame, label, warning_count, consecutive_count):
        cv2.putText(frame, f"Status: {label}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        cv2.putText(frame, f"Warnings: {warning_count}", (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

        cv2.putText(frame, f"Consecutive Drowsy Frames: {consecutive_count}", (20, 120),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        return frame
