from sqlalchemy.orm import Session
from models.user import User

class UserRepository:
    """Repositorio para interactuar con la tabla de usuarios."""
    
    def __init__(self, session: Session):
        self.session = session

    def get_by_username(self, username: str) -> User | None:
        return self.session.query(User).filter(User.username == username).first()

    def get_by_id(self, user_id: int) -> User | None:
        return self.session.query(User).filter(User.id == user_id).first()

    def create(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
        
    def update(self) -> None:
        self.session.commit()
