from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from apps.src.infra.sqlalchemy.config.database import get_db
from apps.src.infra.providers import token_providers
from jose import JWTError
from apps.src.infra.sqlalchemy.crud import crud_users


oauth2_schema = OAuth2PasswordBearer (tokenUrl = 'token')


def get_current_user(token: str = Depends(oauth2_schema),
                    session: Session = Depends(get_db)):
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail='Token inválido'
    )

    try:
        email = token_providers.verify_acess_token(token)
    except JWTError:
        raise exception
    
    if not email:
        raise exception

    user = crud_users.CrudUsers.get_user_by_phone_number(email)

    if not user:
        raise exception

    return user