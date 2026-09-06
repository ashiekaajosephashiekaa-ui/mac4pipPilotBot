from fastapi import APIRouter, Request
from aiogram.types import Update
from app.bot.bot import dp, bot
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api", tags=["telegram"])

@router.post("/webhook/telegram")
async def telegram_webhook(request: Request):
    try:
        update_data = await request.json()
        update = Update(**update_data)
        await dp.feed_update(bot, update)
        return {"ok": True}
    except Exception as e:
        logger.error(f"Webhook error: {e}")
        return {"ok": False, "error": str(e)}

@router.get("/webhook/telegram")
async def telegram_webhook_status():
    return {"status": "Webhook is active"}
