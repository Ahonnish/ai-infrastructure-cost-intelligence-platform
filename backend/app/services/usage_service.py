import logging

from sqlalchemy.orm import Session

from app.models.usage_record import UsageRecord
from app.models.user import User
from app.schemas.usage_record import UsageRecordCreate

logger = logging.getLogger(__name__)


class UsageService:

    @staticmethod
    def create_usage_record(
        db: Session,
        usage: UsageRecordCreate,
        current_user: User,
    ):
        logger.info(
            "Creating usage record for user_id=%s",
            current_user.id,
        )

        db_usage = UsageRecord(
            **usage.model_dump(),
            user_id=current_user.id,
        )

        db.add(db_usage)
        db.commit()
        db.refresh(db_usage)

        logger.info(
            "Usage record created successfully with id=%s for user_id=%s",
            db_usage.id,
            current_user.id,
        )

        return db_usage