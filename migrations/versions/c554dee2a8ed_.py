"""empty message

Revision ID: c554dee2a8ed
Revises: 3e0a3909ce9e
Create Date: 2023-10-25 12:19:28.032899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c554dee2a8ed'
down_revision = '3e0a3909ce9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fees', schema=None) as batch_op:
        batch_op.add_column(sa.Column('student_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'students', ['student_id'], ['id'])

    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.drop_column('balance')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.add_column(sa.Column('balance', sa.VARCHAR(), autoincrement=False, nullable=True))

    with op.batch_alter_table('fees', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('student_id')

    # ### end Alembic commands ###
