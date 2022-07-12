"""Add last few columns to posts table

Revision ID: b6e93b82aaab
Revises: 25f9797bac22
Create Date: 2022-07-12 13:44:46.335306

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6e93b82aaab'
down_revision = '25f9797bac22'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                  nullable=False, server_default='True'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('now()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
