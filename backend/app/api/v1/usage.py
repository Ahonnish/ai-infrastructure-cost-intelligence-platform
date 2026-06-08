from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.usage_record import (
    UsageRecordCreate,
    UsageRecordResponse
)
from app.services.usage_service import UsageService

router = APIRouter(
    prefix="/usage",
    tags=["Usage"]
)


@router.post("/", response_model=UsageRecordResponse)
def create_usage_record(
    usage: UsageRecordCreate,
    db: Session = Depends(get_db)
):
    return UsageService.create_usage_record(
        db=db,
        usage=usage
    )