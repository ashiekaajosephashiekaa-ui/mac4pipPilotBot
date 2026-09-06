from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from app.config import config

bot = Bot(token=config.8874261770:AAGQwVFoLAAkQcWXp2pszHPKr8HIIHdP3lg
)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🤖 Welcome to PipPilot AI\n\n"
        "This is a minimal working bot.\n"
        "More features coming soon!"
    )

@dp.message(Command("help"))
async def help_cmd(message: types.Message):
    await message.answer("Use /start to begin.")
