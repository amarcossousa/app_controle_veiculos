"""Added columns in controle for condutor

Revision ID: 0a44533c83e7
Revises: 9a1a0d7aff05
Create Date: 2023-02-22 10:35:15.498656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a44533c83e7'
down_revision = '9a1a0d7aff05'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('controle', sa.Column('objetivo', sa.String(length=80), nullable=True))
    op.add_column('controle', sa.Column('combustivel', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('controle', 'combustivel')
    op.drop_column('controle', 'objetivo')
    # ### end Alembic commands ###
