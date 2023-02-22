from apps.src import schema
from apps.src.infra.sqlalchemy.models import model
from sqlalchemy.orm import Session
from sqlalchemy import Select

class CrudUsers():

    def __init__(self, session: Session):
        self.session = session

    def create_user(self, user: schema.Users):
        db_users = model.Users( name = user.name,
                                email = user.email,
                                phone_number = user.phone_number,
                                password = user.password)
        
        self.session.add(db_users)
        self.session.commit()
        self.session.refresh(db_users)
        return db_users


    def get_all_users(self, user: schema.Users):
        ...
        
    
    def get_user_by_id(self):
        ...
    
    def update_user_by_put(self):
        ...

    def update_user_by_pacth(self):
        ...

        def delete_user(self):
            ...