"""add content column to posts table

Revision ID: ef4e8915ecc8
Revises: fadccd16e0d2
Create Date: 2022-07-12 12:37:02.650942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef4e8915ecc8'
down_revision = 'fadccd16e0d2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
