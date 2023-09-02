from apps.src.infra.sqlalchemy.config.database import criar_db
from fastapi import APIRouter, Depends
from apps.src.infra.providers.token_providers import verify_acess_token

criar_db()
router = APIRouter()

@router.post("/me")
def read_user_me():
    acess_token: Depends(verify_acess_token)