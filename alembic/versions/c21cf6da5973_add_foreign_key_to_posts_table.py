"""add foreign key to posts table

Revision ID: c21cf6da5973
Revises: 5d0ececfa51e
Create Date: 2022-07-14 12:07:15.285202

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c21cf6da5973'
down_revision = '5d0ececfa51e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'owner_id', sa.Integer(), nullable=False)),
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users', local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
