"""empty message

Revision ID: 947100f21519
Revises: 402d4d383b94
Create Date: 2023-11-15 10:40:59.573451

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '947100f21519'
down_revision = '402d4d383b94'
branch_labels = None
depends_on = None


def upgrade():
    # ... existing code ...
    op.add_column('users', sa.Column('image_file', sa.String(length=100), nullable=False, server_default='default.jpg'))

def downgrade():
    # ... existing code ...
    op.drop_column('users', 'image_file')