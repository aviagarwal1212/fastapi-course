"""add content column to post table

Revision ID: ae4cd47eeb6b
Revises: 66ddfbd6803e
Create Date: 2022-07-14 11:44:08.821464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae4cd47eeb6b'
down_revision = '66ddfbd6803e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
