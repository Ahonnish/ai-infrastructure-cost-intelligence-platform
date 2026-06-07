from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.usage_record import UsageRecord
from app.schemas import (
    UsageRecordCreate,
    UsageRecordResponse
)

router = APIRouter(
    prefix="/usage",
    tags=["Usage"]
)


@router.post(
    "/",
    response_model=UsageRecordResponse
)
def create_usage_record(
    payload: UsageRecordCreate,
    db: Session = Depends(get_db)
):
    usage_record = UsageRecord(
        provider=payload.provider,
        model_name=payload.model_name,
        input_tokens=payload.input_tokens,
        output_tokens=payload.output_tokens,
        total_tokens=payload.total_tokens,
        cost=payload.cost,
        request_count=payload.request_count
    )

    db.add(usage_record)
    db.commit()
    db.refresh(usage_record)

    return usage_record