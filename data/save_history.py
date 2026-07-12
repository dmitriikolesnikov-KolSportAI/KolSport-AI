import csv
from datetime import datetime


def save_history(name, recovery, fatigue):
    with open("data/history.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d"),
            name,
            recovery,
            fatigue
        ])