"""empty message

Revision ID: 01b665d27506
Revises: 2e8ec0beacbd
Create Date: 2023-11-14 16:51:35.769443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01b665d27506'
down_revision = '2e8ec0beacbd'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('users', sa.Column('image_file', sa.String(), nullable=True))
