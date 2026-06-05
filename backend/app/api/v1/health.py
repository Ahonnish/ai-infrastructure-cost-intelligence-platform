from fastapi import APIRouter
from sqlalchemy import text

from app.db.database import engine


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


@router.get("/db")
def database_health():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "database": "connected"
        }

    except Exception as e:
        return {
            "database": "disconnected",
            "error": str(e)
        }