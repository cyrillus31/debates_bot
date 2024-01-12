"""create topics table

Revision ID: 8d2e7578829f
Revises: 
Create Date: 2024-01-12 23:58:04.731020

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8d2e7578829f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
            "topics",
            sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
            sa.Column("text", sa.String(500), nullable=False),
            sa.Column("frequency", sa.Integer, default=0),
            sa.Column("language", sa.String(3)),
            )
    


def downgrade() -> None:
    op.drop_table("topics")
