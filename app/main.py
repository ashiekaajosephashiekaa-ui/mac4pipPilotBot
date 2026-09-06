import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.telegram import router as telegram_router
from app.bot.bot import bot
from app.config import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting PipPilot bot service")
    try:
        if config.TELEGRAM_WEBHOOK_URL:
            await bot.set_webhook(url=config.TELEGRAM_WEBHOOK_URL)
            logger.info(f"Webhook set to {config.TELEGRAM_WEBHOOK_URL}")
        else:
            logger.warning("TELEGRAM_WEBHOOK_URL not set. Bot won't receive updates.")
    except Exception as e:
        logger.error(f"Startup error: {e}")
    
    yield
    
    # Shutdown
    logger.info("Shutting down")
    try:
        await bot.session.close()
    except Exception as e:
        logger.error(f"Shutdown error: {e}")

app = FastAPI(lifespan=lifespan)
app.include_router(health_router)
app.include_router(telegram_router)
