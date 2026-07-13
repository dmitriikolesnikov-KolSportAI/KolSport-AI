from dotenv import load_dotenv
import os
from garminconnect import Garmin

load_dotenv()

email = os.getenv("GARMIN_EMAIL")
password = os.getenv("GARMIN_PASSWORD")

try:
    client = Garmin(email, password)
    client.login()

    print("✅ Успешный вход в Garmin Connect!")

except Exception as e:
    print(f"❌ Ошибка: {e}")