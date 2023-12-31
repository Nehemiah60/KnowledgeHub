"""empty message

Revision ID: 156fdf18b93d
Revises: a92ba8ae50df
Create Date: 2023-10-27 13:49:27.532408

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '156fdf18b93d'
down_revision = 'a92ba8ae50df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fees', schema=None) as batch_op:
        batch_op.drop_constraint('fees_student_id_fkey', type_='foreignkey')
        batch_op.drop_column('student_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fees', schema=None) as batch_op:
        batch_op.add_column(sa.Column('student_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('fees_student_id_fkey', 'students', ['student_id'], ['id'])

    # ### end Alembic commands ###
