"""empty message

Revision ID: 150bd0246747
Revises: f9354a48d407
Create Date: 2018-05-17 10:52:20.248499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '150bd0246747'
down_revision = 'f9354a48d407'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.Unicode(), nullable=True),
    sa.Column('description', sa.Unicode(), nullable=True),
    sa.Column('creation_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code'),
    schema='dbqrest'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('questions', schema='dbqrest')
    # ### end Alembic commands ###
