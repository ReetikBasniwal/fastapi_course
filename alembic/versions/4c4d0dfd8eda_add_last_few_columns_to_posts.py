"""add last few columns to posts

Revision ID: 4c4d0dfd8eda
Revises: 9dbdc19bcd50
Create Date: 2025-10-17 21:10:19.025347

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4c4d0dfd8eda'
down_revision: Union[str, Sequence[str], None] = '9dbdc19bcd50'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column(
                    'published', sa.Boolean(), nullable=False, server_default='TRUE'
                    ))
    op.add_column('posts',sa.Column(
                      'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')
                  ))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
