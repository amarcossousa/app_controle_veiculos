from fastapi import APIRouter, status, Depends, HTTPException
from apps.src.schema import Users, UsersSimple, LoginSucess, LoginData
from apps.src.infra.sqlalchemy.crud.crud_users import CrudUsers
from sqlalchemy.orm import Session
from apps.src.infra.sqlalchemy.config.database import get_db
from apps.src.infra.sqlalchemy.config.database import criar_db
from apps.src.infra.providers import hash_providers, token_providers
from apps.src.router.routers_utils import get_current_user
from apps.src.infra.providers.token_providers import verify_acess_token

criar_db()
router = APIRouter()

@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=UsersSimple)
def signup(user: Users, session: Session = Depends(get_db)):
    user_locate = CrudUsers(session).get_user_by_email(user.email)
    if user_locate:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Usuário já cadastrado para esse e-mail')
    user.password = hash_providers.generate_hash(user.password)
    user_created = CrudUsers(session).create_user(user)
    return user_created


@router.post('/token', response_model=LoginSucess, status_code=status.HTTP_202_ACCEPTED)
async def login(login_data: LoginData, session: Session = Depends(get_db)):
    email = login_data.email
    password = login_data.password
    

    user = CrudUsers(session).get_user_by_email(email)

    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail= 'E-mail ou senha não confere!')
    
    password_validate = hash_providers.verify_hash(password, user.password)
    if not password_validate:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='E-mail ou senha não confere!')
    token = token_providers.create_acess_token({'sub': user.email})
    return LoginSucess(user=user, acess_token=token)


@router.delete('/user/{id}')
def remove_user(id: int, session: Session = Depends(get_db), user = Depends(get_current_user)):
    user = CrudUsers(session).get_user(id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Usuário não encontrato')
    CrudUsers(session).delete_user(id)
    return {'msg': 'Usuário removido com sucesso'}

# não encontra o id e não retorna a lista completa 
# @router.get("/user/", response_model=UsersSimple)
# def get_all_user(session: Session = Depends(get_db)):
#     users = CrudUsers(session).get_all_users()
#     return users

@router.get("/me", response_model= UsersSimple)
def read_user_me(user: Users = Depends (get_current_user)):
    return user
    
