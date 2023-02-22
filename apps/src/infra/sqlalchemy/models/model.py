from sqlalchemy import Column, String, Integer, DateTime, Boolean
from apps.src.infra.sqlalchemy.config.database import Base
from datetime import datetime

now = datetime.now()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    password = Column(String)
    created = Column(DateTime, default=now.strftime("%d/%m/%Y, %H:%M:%S"))
    is_active = Column(Boolean, default= True) 
    is_admin = Column(Boolean, default= False)


class Veiculos(Base):
    __tablename__ = 'veiculos'
    id = Column(Integer, primary_key=True, index=True)
    yers = Column(String)
    model = Column(String)
    fabricante = Column(String)
    is_available = Column(Boolean, default=False)
    created = Column(DateTime, default=datetime.now())
    

class ControleKm(Base):
    __tablename__ = 'controle'
    id = Column(Integer, primary_key=True, index=True)
    destino = Column(String)
    km_inicial = Column(Integer)
    km_final = Column(Integer)
    objetivo = Column(String(80))
    combustivel = Column(Integer)

    

