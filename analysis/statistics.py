def average_recovery(history):
    if len(history) == 0:
        return None

    total = 0

    for day in history:
        total += float(day["recovery"])

    return total / len(history)