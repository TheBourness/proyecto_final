import customtkinter as ctk
from views.components.sidebar import Sidebar
from views.components.topbar import Topbar
from config import COLOR_PALETTE

class AppView(ctk.CTkFrame):
    """Vista principal de la aplicación (Layout con Sidebar y Content Area)."""
    
    def __init__(self, parent, user, logout_callback):
        super().__init__(parent, fg_color=COLOR_PALETTE["black"], corner_radius=0)
        self.parent = parent
        self.user = user
        self.logout_callback = logout_callback
        
        self._setup_layout()

    def _setup_layout(self):
        # Configurar grid principal
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # Sidebar (Columna 0)
        self.sidebar = Sidebar(self, command_callback=self.on_sidebar_click)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        # Contenedor derecho para Topbar y Contenido (Columna 1)
        self.right_container = ctk.CTkFrame(self, fg_color=COLOR_PALETTE["bg_app"], corner_radius=0)
        self.right_container.grid(row=0, column=1, sticky="nsew")
        
        self.right_container.grid_rowconfigure(1, weight=1)
        self.right_container.grid_columnconfigure(0, weight=1)
        
        # Topbar (Fila 0 dentro del contenedor derecho)
        self.topbar = Topbar(self.right_container, user_name=self.user.username)
        self.topbar.grid(row=0, column=0, sticky="ew")
        
        # Main Content Frame (Fila 1 dentro del contenedor derecho)
        self.content_frame = ctk.CTkFrame(self.right_container, fg_color=COLOR_PALETTE["bg_app"], corner_radius=0)
        self.content_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        
        # Diccionario para almacenar las vistas de cada sección
        self.frames = {}

    def on_sidebar_click(self, view_name: str):
        if view_name == "Logout":
            self.logout_callback()
            return
            
        self.topbar.set_section(view_name)
        self.show_frame(view_name)

    def show_frame(self, view_name: str):
        # Ocultar todos los frames
        for frame in self.frames.values():
            frame.pack_forget()
            
        # Mostrar el frame solicitado
        if view_name in self.frames:
            self.frames[view_name].pack(fill="both", expand=True)
