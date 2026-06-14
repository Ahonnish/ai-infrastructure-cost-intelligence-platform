import logging

from sqlalchemy.orm import Session

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)
from app.models.user import User
from app.schemas.user import (
    UserCreate,
    UserLogin
)

logger = logging.getLogger(__name__)


class AuthService:

    @staticmethod
    def register_user(
        db: Session,
        user: UserCreate
    ):
        existing_user = (
            db.query(User)
            .filter(User.email == user.email)
            .first()
        )

        if existing_user:
            raise ValueError(
                "User with this email already exists"
            )

        db_user = User(
            email=user.email,
            username=user.username,
            hashed_password=hash_password(
                user.password
            )
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        logger.info(
            f"User registered successfully: {db_user.email}"
        )

        return db_user

    @staticmethod
    def login_user(
        db: Session,
        user_credentials: UserLogin
    ):
        user = (
            db.query(User)
            .filter(
                User.email == user_credentials.email
            )
            .first()
        )

        if not user:
            return None

        if not verify_password(
            user_credentials.password,
            user.hashed_password
        ):
            return None

        access_token = create_access_token(
            {
                "sub": user.email
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }