import csv


def load_history():
    with open("data/history.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)