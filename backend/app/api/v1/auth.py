from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.common import ApiResponse
from app.schemas.user import (
    UserCreate,
    UserLogin,
    UserResponse
)
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=ApiResponse
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    created_user = AuthService.register_user(
        db=db,
        user=user
    )

    return {
        "success": True,
        "message": "User registered successfully",
        "data": UserResponse.model_validate(
            created_user
        )
    }


@router.post(
    "/login",
    response_model=ApiResponse
)
def login(
    credentials: UserLogin,
    db: Session = Depends(get_db)
):
    token = AuthService.login_user(
        db=db,
        user_credentials=credentials
    )

    if token is None:
        return {
            "success": False,
            "message": "Invalid credentials",
            "data": None
        }

    return {
        "success": True,
        "message": "Login successful",
        "data": token
    }