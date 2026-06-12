import logging

from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta, UTC

from app.models.usage_record import UsageRecord

logger = logging.getLogger(__name__)

class AnalyticsService:

    @staticmethod
    def get_summary(db: Session):
        
        logger.info("Generating analytics summary")
        
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

    @staticmethod
    def get_provider_breakdown(db: Session):
        
        logger.info("Generating provider breakdown")
        
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

    @staticmethod
    def get_model_breakdown(db: Session):
        logger.info("Generating model breakdown")
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

    @staticmethod
    def get_cost_trends(db: Session, days: int = 30):
        
        logger.info(f"Generating cost trends for last {days} days")
        
        cutoff_date = datetime.now(UTC) - timedelta(days=days)

        results = (
            db.query(
                func.date(UsageRecord.created_at).label("date"),
                func.sum(UsageRecord.cost).label("cost")
            )
            .filter(UsageRecord.created_at >= cutoff_date)
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

    @staticmethod
    def get_dashboard(db: Session, days: int = 30):
        
        logger.info("Generating dashboard analytics")
        
        return {
            "summary": AnalyticsService.get_summary(db),
            "providers": AnalyticsService.get_provider_breakdown(db),
            "models": AnalyticsService.get_model_breakdown(db),
            "trends": AnalyticsService.get_cost_trends(db, days),
        }