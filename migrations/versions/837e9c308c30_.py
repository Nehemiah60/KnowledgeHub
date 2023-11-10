"""empty message

Revision ID: 837e9c308c30
Revises: 5f345b78c023
Create Date: 2023-10-24 11:51:08.419290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '837e9c308c30'
down_revision = '5f345b78c023'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=100), nullable=True))
        batch_op.drop_index('ix_students_emai')
        batch_op.create_index(batch_op.f('ix_students_email'), ['email'], unique=True)
        batch_op.drop_column('emai')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.add_column(sa.Column('emai', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
        batch_op.drop_index(batch_op.f('ix_students_email'))
        batch_op.create_index('ix_students_emai', ['emai'], unique=False)
        batch_op.drop_column('email')

    # ### end Alembic commands ###
