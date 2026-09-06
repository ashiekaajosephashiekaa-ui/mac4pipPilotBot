import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TELEGRAM_BOT_TOKEN = os.getenv("HTTP API:
8874261770:AAGQwVFoLAAkQcWXp2pszHPKr8HIIHdP3lg")
    PORT = int(os.getenv("PORT", 8000))

config = Config()
