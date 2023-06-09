"""adicionar_tabela_controle_km

Revision ID: be9a6155680f
Revises: 69afdebdbc5b
Create Date: 2023-03-25 18:20:55.667108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be9a6155680f'
down_revision = '69afdebdbc5b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('controle', sa.Column('data', sa.String(), nullable=True))
    op.add_column('controle', sa.Column('hora_saida', sa.String(), nullable=True))
    op.add_column('controle', sa.Column('hora_chegada', sa.String(), nullable=True))
    op.add_column('controle', sa.Column('tec_responsavel', sa.String(), nullable=True))
    op.add_column('controle', sa.Column('projeto', sa.String(), nullable=True))
    op.add_column('controle', sa.Column('qt_combustivel', sa.Integer(), nullable=True))
    op.add_column('controle', sa.Column('created', sa.DateTime(), nullable=True))
    op.drop_column('controle', 'combustivel')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('controle', sa.Column('combustivel', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('controle', 'created')
    op.drop_column('controle', 'qt_combustivel')
    op.drop_column('controle', 'projeto')
    op.drop_column('controle', 'tec_responsavel')
    op.drop_column('controle', 'hora_chegada')
    op.drop_column('controle', 'hora_saida')
    op.drop_column('controle', 'data')
    # ### end Alembic commands ###
