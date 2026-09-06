from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from app.config import config

bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🤖 Welcome to PipPilot AI\n\n"
        "Your AI-powered Forex strategy automation assistant.\n\n"
        "This bot is online and ready! 🚀"
    )

@dp.message(Command("help"))
async def help_cmd(message: types.Message):
    await message.answer(
        "📖 Help\n\n"
        "Commands:\n"
        "/start - Welcome message\n"
        "/help - This help message"
    )
