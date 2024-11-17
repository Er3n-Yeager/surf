from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")


class Telegram:
    API_ID = int(getenv("API_ID", "12862156"))
    API_HASH = getenv("API_HASH", "d913a2ef10183c683144ff851481d9fd")
    BOT_TOKEN = getenv("BOT_TOKEN", "7575485156:AAEiMwxf3LLL8DurCTlHVnnEmm6WxX_AP6Q")
    PORT = int(getenv("PORT", 8080))
    SESSION_STRING = getenv("SESSION_STRING", "")
    BASE_URL = getenv("BASE_URL", "https://sporting-jemmy-surftg6807-f51abccf.koyeb.app")
    DATABASE_URL = getenv("DATABASE_URL", "mongodb+srv://muthu2:muthu2@cluster0.u0sdu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    AUTH_CHANNEL = [channel.strip() for channel in getenv("AUTH_CHANNEL", " -1002260378612" ).split(",")]
    THEME = getenv("THEME", "quartz").lower()
    USERNAME = getenv("USERNAME", "admin")
    PASSWORD = getenv("PASSWORD", "admin")
    ADMIN_USERNAME = getenv("ADMIN_USERNAME", "surfTG")
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "surfTG")
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '10'))
    MULTI_CLIENT = bool(getenv('MULTI_CLIENT', 'False'))
    HIDE_CHANNEL = bool(getenv('HIDE_CHANNEL', 'False'))
