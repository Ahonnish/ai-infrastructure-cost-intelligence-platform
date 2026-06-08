from sqlalchemy.orm import Session

from app.models.usage_record import UsageRecord
from app.schemas.usage_record import UsageRecordCreate


class UsageService:

    @staticmethod
    def create_usage_record(
        db: Session,
        usage: UsageRecordCreate
    ):
        db_usage = UsageRecord(**usage.model_dump())

        db.add(db_usage)
        db.commit()
        db.refresh(db_usage)

        return db_usage