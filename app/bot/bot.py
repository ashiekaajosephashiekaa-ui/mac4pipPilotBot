from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from app.config import config
import logging

logger = logging.getLogger(__name__)

# Create bot and dispatcher - NO POLLING
bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🤖 Welcome to PipPilot\n\n"
        "📈 Forex Updates\n"
        "Use /forex to check latest rates\n\n"
        "/help - Show commands"
    )

@dp.message(Command("forex"))
async def forex(message: types.Message):
    # Placeholder for forex data
    await message.answer(
        "📊 Current Rates:\n\n"
        "EURUSD: 1.0950\n"
        "GBPUSD: 1.2750\n"
        "USDJPY: 149.50\n\n"
        "Updated just now ✓"
    )

@dp.message(Command("help"))
async def help_cmd(message: types.Message):
    await message.answer(
        "Available Commands:\n\n"
        "/start - Welcome\n"
        "/forex - Current forex rates\n"
        "/help - This menu"
    )

@dp.message()
async def echo(message: types.Message):
    await message.answer("I didn't understand that. Use /help for commands.")
