"""add user ownership to usage records

Revision ID: be8e534fc427
Revises: c205d31c4220
Create Date: 2026-08-12 19:04:31.446285
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "be8e534fc427"
down_revision: Union[str, Sequence[str], None] = "c205d31c4220"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    with op.batch_alter_table("usage_records") as batch_op:
        batch_op.add_column(
            sa.Column("user_id", sa.Integer(), nullable=False)
        )
        batch_op.create_index(
            "ix_usage_records_user_id",
            ["user_id"],
            unique=False,
        )
        batch_op.create_foreign_key(
            "fk_usage_records_user_id_users",
            "users",
            ["user_id"],
            ["id"],
        )


def downgrade() -> None:
    """Downgrade schema."""

    with op.batch_alter_table("usage_records") as batch_op:
        batch_op.drop_constraint(
            "fk_usage_records_user_id_users",
            type_="foreignkey",
        )
        batch_op.drop_index("ix_usage_records_user_id")
        batch_op.drop_column("user_id")