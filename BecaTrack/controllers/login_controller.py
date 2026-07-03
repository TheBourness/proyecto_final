from views.login_view import LoginView
from services.auth_service import AuthService
import customtkinter as ctk
# Aquí importaremos MainController más adelante en la Fase 6

class LoginController:
    """Controlador que maneja la lógica de la pantalla de Login."""
    
    def __init__(self, view: LoginView, auth_service: AuthService, root: ctk.CTk, session):
        self.view = view
        self.auth_service = auth_service
        self.root = root
        self.session = session
        
        # Conectar los eventos de los botones de la vista con este controlador
        self.view.login_button.configure(command=self.handle_login)
        self.view.toggle_password_btn.configure(command=self.toggle_password)

    def handle_login(self):
        username = self.view.username_entry.get()
        password = self.view.password_entry.get()
        
        if not username or not password:
            self.view.show_error("Por favor, ingresa usuario y contraseña.")
            return
            
        user = self.auth_service.authenticate(username, password)
        if user:
            self.view.show_success("Login exitoso. Cargando sistema...")
            print(f"[{user.username}] ha ingresado al sistema.")
            
            # Destruir login visual y cargar app principal
            self.view.pack_forget()
            from views.app_view import AppView
            from controllers.main_controller import MainController
            
            app_view = AppView(self.root, user, self.handle_logout)
            main_ctrl = MainController(app_view, self.session)
            app_view.pack(fill="both", expand=True)
        else:
            self.view.show_error("Credenciales incorrectas.")

    def handle_logout(self):
        # Limpiar root y volver al login
        for child in self.root.winfo_children():
            child.pack_forget()
        self.view.pack(fill="both", expand=True)
        self.view.username_entry.delete(0, 'end')
        self.view.password_entry.delete(0, 'end')
        self.view.message_label.configure(text="")

    def toggle_password(self):
        current_show = self.view.password_entry.cget("show")
        if current_show == "*":
            self.view.password_entry.configure(show="")
            self.view.toggle_password_btn.configure(text="Ocultar")
        else:
            self.view.password_entry.configure(show="*")
            self.view.toggle_password_btn.configure(text="Mostrar")
