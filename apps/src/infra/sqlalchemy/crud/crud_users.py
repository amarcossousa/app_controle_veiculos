from apps.src import schema
from apps.src.infra.sqlalchemy.models import model
from sqlalchemy.orm import Session
from sqlalchemy import select, delete

class CrudUsers():

    def __init__(self, session: Session):
        self.session = session

    def create_user(self, user: schema.Users):
        db_users = model.Users( 
              name = user.name,
              email = user.email,
              password = user.password
          )
        
        self.session.add(db_users)
        self.session.commit()
        self.session.refresh(db_users)
        return db_users


    def get_all_users(self):
        stmt = select(model.Users)
        users = self.session.execute(stmt).scalars().all()
        return users 
    
    def get_user_by_email(self, email):
        query = select(model.Users).where(model.Users.email == email)
        return self.session.execute(query).scalars().first()


    def delete_user(self, user_id: int):
        stmt = delete(model.Users).where(model.Users.id == user_id)
        self.session.execute(stmt)
        self.session.commit()
    
    def get_user(self, user_id: int):
        query =select(model.Users).where(model.Users.id == user_id)
        return self.session.execute(query).scalar()
            