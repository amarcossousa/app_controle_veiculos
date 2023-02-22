from fastapi import APIRouter, status, Depends, HTTPException
from apps.src.schema import Users, UsersSimple
from apps.src.infra.sqlalchemy.crud.crud_users import CrudUsers
from sqlalchemy.orm import Session
from apps.src.infra.sqlalchemy.config.database import get_db
from apps.src.infra.sqlalchemy.config.database import criar_db
from sqlalchemy import Select

criar_db()
router = APIRouter()

@router.post("/user/", status_code=status.HTTP_201_CREATED, response_model=UsersSimple)
def creat_user(user: Users, session: Session = Depends(get_db)):
    user_created = CrudUsers(session).create_user(user)
    return user_created


# @router.get("/user/")
# def get_all_user( session: Session = Depends(get_db)):
#     get_users = session.query(Select).all()
#     return get_users
