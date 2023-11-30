"""empty message

Revision ID: 52aaa0384129
Revises: 90b4203315a2
Create Date: 2023-11-29 09:06:03.849962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52aaa0384129'
down_revision = '90b4203315a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('parent_module_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('parent_module_id',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=True)
    )
    # ### end Alembic commands ###
