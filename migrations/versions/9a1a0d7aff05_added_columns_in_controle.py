"""Added columns in controle

Revision ID: 9a1a0d7aff05
Revises: c4538140cbbd
Create Date: 2023-02-22 08:57:42.934971

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9a1a0d7aff05'
down_revision = 'c4538140cbbd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_veiculos_id', table_name='veiculos')
    op.drop_table('veiculos')
    op.drop_index('ix_users_id', table_name='users')
    op.drop_table('users')
    op.drop_index('ix_controle_id', table_name='controle')
    op.drop_table('controle')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('controle',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('destino', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='controle_pkey')
    )
    op.create_index('ix_controle_id', 'controle', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('phone_number', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('is_admin', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey')
    )
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    op.create_table('veiculos',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('yers', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('model', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('fabricante', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('is_available', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='veiculos_pkey')
    )
    op.create_index('ix_veiculos_id', 'veiculos', ['id'], unique=False)
    # ### end Alembic commands ###
