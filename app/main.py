import asyncio
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.health import router as health_router
from app.bot.bot import init_bot, dp
from app.config import config
import uvicorn

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        bot = init_bot()
        logger.info("Starting bot polling")
        asyncio.create_task(dp.start_polling(bot))
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(health_router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=config.PORT)
