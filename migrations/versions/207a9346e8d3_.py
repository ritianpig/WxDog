"""empty message

Revision ID: 207a9346e8d3
Revises: 3c383133008b
Create Date: 2019-04-18 13:44:18.377717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '207a9346e8d3'
down_revision = '3c383133008b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_buys', sa.Column('buydate', sa.DateTime(), nullable=True, comment='购买时间'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_buys', 'buydate')
    # ### end Alembic commands ###
