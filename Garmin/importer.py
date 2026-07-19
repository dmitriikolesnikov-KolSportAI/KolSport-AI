from datetime import date


def get_recovery_data(client):
    today = date.today().strftime("%Y-%m-%d")

    sleep_data = client.get_sleep_data(today)

    sleep = sleep_data["dailySleepDTO"]

    recovery_data = {
        "date": sleep["calendarDate"],

        # Sleep
        "sleep_seconds": sleep["sleepTimeSeconds"],
        "deep_sleep_seconds": sleep["deepSleepSeconds"],
        "light_sleep_seconds": sleep["lightSleepSeconds"],
        "rem_sleep_seconds": sleep["remSleepSeconds"],
        "awake_seconds": sleep["awakeSleepSeconds"],

        # Heart
        "avg_sleep_hr": sleep["avgHeartRate"],

        # Recovery
        "hrv": sleep_data["avgOvernightHrv"],
        "resting_hr": sleep_data["restingHeartRate"],
    }

    return recovery_data