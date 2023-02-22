from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey
from apps.src.infra.sqlalchemy.config.database import Base
from datetime import datetime

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    password = Column(String)
    created = Column(DateTime, default=datetime.now())
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
    

