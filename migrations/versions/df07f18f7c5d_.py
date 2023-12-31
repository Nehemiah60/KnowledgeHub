"""empty message

Revision ID: df07f18f7c5d
Revises: ddd9a1893339
Create Date: 2023-12-01 08:56:18.736397

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df07f18f7c5d'
down_revision = 'ddd9a1893339'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('course', schema=None) as batch_op:
        batch_op.add_column(sa.Column('enrolled_user', sa.Integer(), nullable=True))
        batch_op.drop_constraint('course_user_fkey', type_='foreignkey')
        batch_op.drop_column('user')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('course', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('course_user_fkey', 'users', ['user'], ['id'])
        batch_op.drop_column('enrolled_user')

    # ### end Alembic commands ###
