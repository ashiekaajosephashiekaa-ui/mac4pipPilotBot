from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health():
    return {"status": "ok", "service": "PipPilot"}

@router.get("/")
async def root():
    return {"message": "PipPilot Forex Bot API"}
