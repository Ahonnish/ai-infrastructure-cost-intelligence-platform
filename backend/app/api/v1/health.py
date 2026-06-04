from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)

@router.get("/")
def health_check():
    return {
        "status": "healthy",
        "service": "AI Cost Intelligence Platform API"
    }

@router.get("/ping")
def ping():
    return {
        "message": "pong"
    }