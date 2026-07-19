from dotenv import load_dotenv
import os
from garminconnect import Garmin
from garmin.importer import get_recovery_data

load_dotenv()


def get_garmin_data():
    email = os.getenv("GARMIN_EMAIL")
    password = os.getenv("GARMIN_PASSWORD")

    client = Garmin(email, password)
    client.login()

    print("✅ Успешный вход в Garmin Connect!")

    recovery_data = get_recovery_data(client)

    return recovery_data