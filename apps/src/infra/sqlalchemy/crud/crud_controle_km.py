from apps.src import schema
from apps.src.infra.sqlalchemy.models.model import ControleKm
from sqlalchemy.orm import Session

class VeiculosCrud:
    def __init__(self, session = Session):
        self.session = session
    

    def create_new_controle(self, controle: schema.ControleKm):
        db_controle = ControleKm(
            data = controle.data,
            destino = controle.destino,
            hora_saida = controle.hora_saida,
            hora_chegada = controle.hora_chegada,
            km_inicial = controle.km_inicial,
            km_final = controle.km_final,
            objetivo = controle.objetivo,
            tec_responsavel = controle.tec_responsavel,
            projeto = controle.projeto,
            qt_combustivel = controle.qt_combustivel
        )
        self.session.add(db_controle)
        self.session.commit()
        self.session.refresh(db_controle)
        return db_controle