from datetime import datetime

class AdaptiveLogic:
    def __init__(self):
        self.warning_count = 0
        self.consecutive_drowsy = 0

    def get_dynamic_threshold(self):
        hour = datetime.now().hour

        if hour >= 22 or hour <= 5:
            return 2
        return 4

    def update_state(self, prediction):
        if prediction == 0:
            self.consecutive_drowsy = 0
        else:
            self.consecutive_drowsy += 1

    def should_trigger_severe(self):
        threshold = self.get_dynamic_threshold()

        if self.warning_count >= 2:
            threshold -= 1

        threshold = max(1, threshold)

        return self.consecutive_drowsy >= threshold
