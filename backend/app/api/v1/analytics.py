from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.db.session import get_db
from app.models.usage_record import UsageRecord

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/summary")
def get_summary(db: Session = Depends(get_db)):
    total_cost = db.query(
        func.coalesce(func.sum(UsageRecord.cost), 0)
    ).scalar()

    total_tokens = db.query(
        func.coalesce(func.sum(UsageRecord.total_tokens), 0)
    ).scalar()

    total_requests = db.query(
        func.coalesce(func.sum(UsageRecord.request_count), 0)
    ).scalar()

    return {
        "total_cost": float(total_cost),
        "total_tokens": total_tokens,
        "total_requests": total_requests,
    }