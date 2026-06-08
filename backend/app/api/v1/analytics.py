from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.analytics_service import AnalyticsService

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/summary")
def get_summary(db: Session = Depends(get_db)):
    return AnalyticsService.get_summary(db)


@router.get("/providers")
def get_provider_breakdown(db: Session = Depends(get_db)):
    return AnalyticsService.get_provider_breakdown(db)


@router.get("/models")
def get_model_breakdown(db: Session = Depends(get_db)):
    return AnalyticsService.get_model_breakdown(db)


@router.get("/trends")
def get_cost_trends(
    days: int = 30,
    db: Session = Depends(get_db)
):
    return AnalyticsService.get_cost_trends(db, days)


@router.get("/dashboard")
def get_dashboard(
    days: int = 30,
    db: Session = Depends(get_db)
):
    return AnalyticsService.get_dashboard(db, days)