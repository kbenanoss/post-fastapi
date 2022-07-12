"""Add user table

Revision ID: e9bfd1bd03e9
Revises: ef4e8915ecc8
Create Date: 2022-07-12 12:44:57.663800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9bfd1bd03e9'
down_revision = 'ef4e8915ecc8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('phone', sa.String(),
                              nullable=True, unique=True),
                    sa.Column('created_at', sa.TIMESTAMP(
                        timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
