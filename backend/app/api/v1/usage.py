from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.common import ApiResponse
from app.schemas.usage_record import (
    UsageRecordCreate,
    UsageRecordResponse,
)
from app.services.usage_service import UsageService

router = APIRouter(
    prefix="/usage",
    tags=["Usage"],
)

@router.post("/", response_model=ApiResponse)
def create_usage_record(
    usage: UsageRecordCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    record = UsageService.create_usage_record(
        db=db,
        usage=usage,
        current_user=current_user,
    )
    return {
        "success": True,
        "message": "Usage record created successfully",
        "data": UsageRecordResponse.model_validate(record),
    }