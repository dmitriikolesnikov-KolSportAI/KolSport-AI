import sqlite3

DATABASE = "data/athlete.db"


def create_database():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recovery (
            date TEXT PRIMARY KEY,
            sleep_seconds INTEGER,
            deep_sleep_seconds INTEGER,
            light_sleep_seconds INTEGER,
            rem_sleep_seconds INTEGER,
            awake_seconds INTEGER,
            avg_sleep_hr REAL,
            hrv REAL,
            resting_hr INTEGER
        )
    """)

    connection.commit()
    connection.close()


def save_recovery(data):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO recovery
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["date"],
        data["sleep_seconds"],
        data["deep_sleep_seconds"],
        data["light_sleep_seconds"],
        data["rem_sleep_seconds"],
        data["awake_seconds"],
        data["avg_sleep_hr"],
        data["hrv"],
        data["resting_hr"]
    ))

    connection.commit()
    connection.close()