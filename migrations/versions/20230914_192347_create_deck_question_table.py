"""create deck_question table

Revision ID: 4bdcab12115b
Revises: d700dbca29f0
Create Date: 2023-09-14 19:23:47.535477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4bdcab12115b'
down_revision = 'd700dbca29f0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('deck_questions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('deck_id', sa.Integer(), sa.ForeignKey('decks.id'), nullable=False),
    sa.Column('question_id', sa.Integer(), sa.ForeignKey('questions.id'), nullable=False)
    )


def downgrade():
    op.drop_table('deck_questions')
