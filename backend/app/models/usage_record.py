from datetime import datetime, UTC

from sqlalchemy import DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class UsageRecord(Base):
    __tablename__ = "usage_records"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    provider: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    model_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    input_tokens: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    output_tokens: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    total_tokens: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    cost: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    request_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(UTC)
    )