import pandas as pd
from datetime import datetime

class ReportModule:
    def __init__(self):
        self.data = []

    def log_event(self, label, warning_count):
        self.data.append({
            "time": datetime.now().strftime("%H:%M:%S"),
            "label": label,
            "warnings": warning_count
        })

    def save_report(self):
        df = pd.DataFrame(self.data)
        filename = f"reports/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(filename, index=False)
        print(f"Report saved: {filename}")
