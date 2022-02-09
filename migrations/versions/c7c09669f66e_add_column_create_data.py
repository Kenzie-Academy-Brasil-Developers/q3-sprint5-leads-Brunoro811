"""add column create_data

Revision ID: c7c09669f66e
Revises: ec7d7ca51137
Create Date: 2022-02-09 12:02:14.932451

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7c09669f66e'
down_revision = 'ec7d7ca51137'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('leads', sa.Column('creation_data', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('leads', 'creation_data')
    # ### end Alembic commands ###
