"""create reviews table

Revision ID: 8faf8605f8f7
Revises: 127a61e89a8d
Create Date: 2023-09-14 19:08:40.249374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8faf8605f8f7'
down_revision = '127a61e89a8d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), autoincrement=True, primary_key=True, nullable=False),
    sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
    sa.Column('deck_id', sa.Integer(), sa.ForeignKey('decks.id'), nullable=False),
    sa.Column('stars', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('reviews')
