"""alter column text of table topic to be under UNIQUE constaint

Revision ID: 7b50aa3110b0
Revises: 8d2e7578829f
Create Date: 2024-01-13 00:22:25.372274

"""
from typing import Sequence, Union

from alembic import op, operations
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7b50aa3110b0'
down_revision: Union[str, None] = '8d2e7578829f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("topics") as batch_op:
        batch_op.create_unique_constraint(constraint_name="uq_text", columns=["text"])


def downgrade() -> None:
    with op.batch_alter_table("topics") as batch_op:
        batch_op.drop_constraint(constraint_name="uq_text", columns=["text"])
