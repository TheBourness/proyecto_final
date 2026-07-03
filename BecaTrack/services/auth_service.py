import bcrypt
from repositories.user_repository import UserRepository
from models.user import User

class AuthService:
    """Servicio para manejar la autenticación y encriptación de contraseñas."""
    
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')

    def check_password(self, password: str, hashed: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

    def authenticate(self, username: str, password: str) -> User | None:
        user = self.user_repo.get_by_username(username)
        if user and user.is_active:
            if self.check_password(password, user.password_hash):
                return user
        return None
