def recovery_trend(history):
    if len(history) < 2:
        return "Недостаточно данных."

    last = float(history[-1]["recovery"])
    previous = float(history[-2]["recovery"])

    if last > previous:
        return "📈 Recovery улучшается."

    elif last < previous:
        return "📉 Recovery снижается."

    else:
        return "➡️ Recovery без изменений."