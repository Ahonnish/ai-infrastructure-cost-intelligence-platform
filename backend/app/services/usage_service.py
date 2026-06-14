import logging

from sqlalchemy.orm import Session

from app.models.usage_record import UsageRecord
from app.schemas.usage_record import UsageRecordCreate


logger = logging.getLogger(__name__)


class UsageService:

    @staticmethod
    def create_usage_record(
        db: Session,
        usage: UsageRecordCreate
    ):
        logger.info("Creating usage record")

        db_usage = UsageRecord(**usage.model_dump())

        db.add(db_usage)
        db.commit()
        db.refresh(db_usage)

        logger.info(
            f"Usage record created successfully with id={db_usage.id}"
        )

        return db_usage