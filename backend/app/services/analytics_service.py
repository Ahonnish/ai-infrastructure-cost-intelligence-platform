import logging
from datetime import UTC, datetime, timedelta

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.usage_record import UsageRecord

logger = logging.getLogger(__name__)


class AnalyticsService:

    @staticmethod
    def get_summary(db: Session, user_id: int):
        logger.info("Generating analytics summary")

        total_cost = (
            db.query(func.coalesce(func.sum(UsageRecord.cost), 0))
            .filter(UsageRecord.user_id == user_id)
            .scalar()
        )

        total_tokens = (
            db.query(func.coalesce(func.sum(UsageRecord.total_tokens), 0))
            .filter(UsageRecord.user_id == user_id)
            .scalar()
        )

        total_requests = (
            db.query(func.coalesce(func.sum(UsageRecord.request_count), 0))
            .filter(UsageRecord.user_id == user_id)
            .scalar()
        )

        return {
            "total_cost": float(total_cost),
            "total_tokens": total_tokens,
            "total_requests": total_requests,
        }

    @staticmethod
    def get_provider_breakdown(db: Session, user_id: int):
        logger.info("Generating provider breakdown")

        results = (
            db.query(UsageRecord.provider, func.sum(UsageRecord.cost).label("cost"))
            .filter(UsageRecord.user_id == user_id)
            .group_by(UsageRecord.provider)
            .all()
        )

        return [{"provider": row.provider, "cost": float(row.cost)} for row in results]

    @staticmethod
    def get_model_breakdown(db: Session, user_id: int):
        logger.info("Generating model breakdown")

        results = (
            db.query(UsageRecord.model_name, func.sum(UsageRecord.cost).label("cost"))
            .filter(UsageRecord.user_id == user_id)
            .group_by(UsageRecord.model_name)
            .all()
        )

        return [
            {"model_name": row.model_name, "cost": float(row.cost)} for row in results
        ]

    @staticmethod
    def get_cost_trends(db: Session, user_id: int, days: int = 30):
        logger.info(f"Generating cost trends for last {days} days")

        cutoff_date = datetime.now(UTC) - timedelta(days=days)

        results = (
            db.query(
                func.date(UsageRecord.created_at).label("date"),
                func.sum(UsageRecord.cost).label("cost"),
            )
            .filter(
                UsageRecord.user_id == user_id, UsageRecord.created_at >= cutoff_date
            )
            .group_by(func.date(UsageRecord.created_at))
            .order_by(func.date(UsageRecord.created_at))
            .all()
        )

        return [{"date": str(row.date), "cost": float(row.cost)} for row in results]

    @staticmethod
    def get_dashboard(db: Session, user_id: int, days: int = 30):
        logger.info("Generating dashboard analytics")

        return {
            "summary": AnalyticsService.get_summary(db, user_id),
            "providers": AnalyticsService.get_provider_breakdown(db, user_id),
            "models": AnalyticsService.get_model_breakdown(db, user_id),
            "trends": AnalyticsService.get_cost_trends(db, user_id, days),
        }
