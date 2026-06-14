from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.common import ApiResponse
from app.schemas.usage_record import UsageRecordCreate
from app.services.usage_service import UsageService
from app.dependencies.auth import get_current_user

router = APIRouter(
    prefix="/usage",
    tags=["Usage"]
)

from app.schemas.usage_record import (
    UsageRecordCreate,
    UsageRecordResponse
)


@router.post("/", response_model=ApiResponse)
def create_usage_record(
    usage: UsageRecordCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    record = UsageService.create_usage_record(
        db=db,
        usage=usage
    )

    return {
        "success": True,
        "message": "Usage record created successfully",
        "data": UsageRecordResponse.model_validate(record)
    }