"""create deck table

Revision ID: 127a61e89a8d
Revises: 8ba652d1ea15
Create Date: 2023-09-14 19:01:04.100624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '127a61e89a8d'
down_revision = '8ba652d1ea15'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('decks',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, primary_key=True),
    sa.Column('user_id', sa.String(), sa.ForeignKey('users.id'), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('category', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('decks')
