"""create incorrect answers table

Revision ID: 39e5cc895897
Revises: 8faf8605f8f7
Create Date: 2023-09-14 19:14:44.432613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39e5cc895897'
down_revision = '8faf8605f8f7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('incorrect_answers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
    sa.Column('question_id', sa.Integer(), sa.ForeignKey('questions.id'), nullable=False),
    )


def downgrade():
    op.drop_table('incorrect_answers')
