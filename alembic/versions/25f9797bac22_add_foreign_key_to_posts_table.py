"""Add foreign-key to posts table

Revision ID: 25f9797bac22
Revises: e9bfd1bd03e9
Create Date: 2022-07-12 13:34:23.915477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25f9797bac22'
down_revision = 'e9bfd1bd03e9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts",
                          referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'ower_id')
    pass
