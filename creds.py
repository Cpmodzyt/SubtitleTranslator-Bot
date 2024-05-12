import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class cred:
    BOT_NAME = os.getenv("BOT_NAME")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "6916875347:AAHYnAt4IERVVcvNCg3eeRljreEoWbbQOe4")  # From botfather
    API_ID = os.getenv(
        "API_ID", "10471716"
    )  # "Get this value from my.telegram.org! Please do not steal"
    API_HASH = os.getenv(
        "API_HASH", "f8a1b21a13af154596e2ff5bed164860"
    )  # "Get this value from my.telegram.org! Please do not steal"
    DB_URL = os.getenv("DB_URL", "https://telegram-bot-51cbb-default-rtdb.firebaseio.com")  # From Firebase database
