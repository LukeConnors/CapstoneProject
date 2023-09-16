"""create messages table

Revision ID: f5ff98046854
Revises: 4bdcab12115b
Create Date: 2023-09-14 19:31:42.999722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5ff98046854'
down_revision = '4bdcab12115b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('messages',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, primary_key=True),
    sa.Column('message', sa.String(), nullable=False),
    sa.Column('sender_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
    sa.Column('recipient_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('messages')
