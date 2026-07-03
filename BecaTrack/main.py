import customtkinter as ctk
import sys
import os

# Configuración del path para evitar errores de importación al ejecutar
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from database.connection import init_db, get_session
from models.user import User
from services.auth_service import AuthService
from repositories.user_repository import UserRepository
from controllers.login_controller import LoginController
from views.login_view import LoginView
from config import APP_TITLE, APP_RESOLUTION, COLOR_PALETTE

def seed_admin_user(auth_service: AuthService, user_repo: UserRepository):
    """Crea un usuario administrador por defecto si la base de datos está vacía."""
    admin = user_repo.get_by_username("admin")
    if not admin:
        hashed = auth_service.hash_password("admin123")
        new_admin = User(username="admin", password_hash=hashed, role="admin")
        user_repo.create(new_admin)
        print("Usuario administrador creado. Credenciales: admin / admin123")

def main():
    # 1. Inicializar Base de Datos (crea becatrack.db y las tablas si no existen)
    init_db()
    
    # 2. Preparar sesión y servicios base
    session = get_session()
    user_repo = UserRepository(session)
    auth_service = AuthService(user_repo)
    
    # Asegurarnos de tener acceso inicial
    seed_admin_user(auth_service, user_repo)
    
    # 3. Configurar CustomTkinter
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    # Inicializar la ventana principal
    app = ctk.CTk()
    app.title(APP_TITLE)
    app.geometry(APP_RESOLUTION)
    app.configure(fg_color=COLOR_PALETTE["black"])
    
    # 4. Iniciar Arquitectura MVC cargando la Vista de Login
    login_view = LoginView(app)
    
    # Inyectar dependencias al Controlador
    login_controller = LoginController(login_view, auth_service, app, session)
    
    # Mostrar la vista llenando toda la pantalla
    login_view.pack(fill="both", expand=True)
    
    # 5. Arrancar Loop de Eventos
    app.mainloop()

if __name__ == "__main__":
    main()
