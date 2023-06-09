"""alter table users

Revision ID: 69afdebdbc5b
Revises: 0a44533c83e7
Create Date: 2023-02-22 12:39:18.253186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69afdebdbc5b'
down_revision = '0a44533c83e7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
