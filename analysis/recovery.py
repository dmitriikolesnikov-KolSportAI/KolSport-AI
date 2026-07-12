def calculate_recovery(sleep_hours, sleep_quality, feeling, legs):
    recovery = (
        sleep_hours * 5 +
        sleep_quality * 4 +
        feeling * 4 -
        legs * 3
    )

    recovery = max(0, min(100, recovery))

    return recovery