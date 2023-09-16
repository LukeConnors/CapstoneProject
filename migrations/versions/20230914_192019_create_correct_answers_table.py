"""create correct answers table

Revision ID: d700dbca29f0
Revises: 39e5cc895897
Create Date: 2023-09-14 19:20:19.731967

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd700dbca29f0'
down_revision = '39e5cc895897'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('correct_answers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, primary_key=True),
    sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
    sa.Column('question_id', sa.Integer(), sa.ForeignKey('questions.id'), nullable=False)
    )


def downgrade():
    op.drop_table('correct_answers')
