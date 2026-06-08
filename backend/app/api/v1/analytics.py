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

@router.get("/providers")
def get_provider_breakdown(db: Session = Depends(get_db)):
    results = (
        db.query(
            UsageRecord.provider,
            func.sum(UsageRecord.cost).label("cost")
        )
        .group_by(UsageRecord.provider)
        .all()
    )

    return [
        {
            "provider": row.provider,
            "cost": float(row.cost)
        }
        for row in results
    ]


@router.get("/models")
def get_model_breakdown(db: Session = Depends(get_db)):
    results = (
        db.query(
            UsageRecord.model_name,
            func.sum(UsageRecord.cost).label("cost")
        )
        .group_by(UsageRecord.model_name)
        .all()
    )

    return [
        {
            "model_name": row.model_name,
            "cost": float(row.cost)
        }
        for row in results
    ]


@router.get("/trends")
def get_cost_trends(db: Session = Depends(get_db)):
    results = (
        db.query(
            func.date(UsageRecord.created_at).label("date"),
            func.sum(UsageRecord.cost).label("cost")
        )
        .group_by(func.date(UsageRecord.created_at))
        .order_by(func.date(UsageRecord.created_at))
        .all()
    )

    return [
        {
            "date": str(row.date),
            "cost": float(row.cost)
        }
        for row in results
    ]