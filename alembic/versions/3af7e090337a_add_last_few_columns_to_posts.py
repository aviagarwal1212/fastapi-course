"""add last few columns to posts

Revision ID: 3af7e090337a
Revises: c21cf6da5973
Create Date: 2022-07-14 12:13:30.090797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3af7e090337a'
down_revision = 'c21cf6da5973'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                                     nullable=False, server_default='TRUE')),
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                     nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
