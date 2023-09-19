"""create the Trivia table

Revision ID: 8ba652d1ea15
Revises: ffdc0a98111c
Create Date: 2023-09-14 18:47:39.796836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ba652d1ea15'
down_revision = 'ffdc0a98111c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('questions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, primary_key=True),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('difficulty', sa.String(), nullable=False),
    sa.Column('question', sa.String(), nullable=False),
    sa.Column('correct_answer', sa.String(), nullable=False),
    sa.Column('incorrect_answers', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('questions')
