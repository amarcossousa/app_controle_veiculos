from fastapi import APIRouter, status, Depends, HTTPException
from apps.src.infra.sqlalchemy.config.database import criar_db, get_db
from apps.src.schema import ControleKm
from sqlalchemy.orm import Session
from apps.src.infra.sqlalchemy.crud.crud_controle_km import VeiculosCrud
from apps.src.router.routers_utils import get_current_user

criar_db()
router = APIRouter()

@router.post("/controles")
def criar_controle(controle: ControleKm, db: Session = Depends(get_db), 
                   user = Depends(get_current_user)):
    controle_criado = VeiculosCrud(db).create_new_controle(controle)
    return controle_criado