import customtkinter as ctk
from config import COLOR_PALETTE

class Topbar(ctk.CTkFrame):
    """Barra superior estilo Web."""
    def __init__(self, parent, user_name="Admin"):
        super().__init__(
            parent, 
            height=80, 
            corner_radius=0, 
            fg_color=COLOR_PALETTE["bg_app"]
        )
        self.grid_propagate(False)
        self.grid_columnconfigure(1, weight=1)
        
        # Títulos
        self.title_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.title_frame.grid(row=0, column=0, padx=30, pady=15, sticky="w")
        
        self.section_title = ctk.CTkLabel(
            self.title_frame, 
            text="Vista General", 
            font=ctk.CTkFont(family="Inter", size=24, weight="bold"),
            text_color=COLOR_PALETTE["text_primary"]
        )
        self.section_title.pack(anchor="w")
        
        self.section_subtitle = ctk.CTkLabel(
            self.title_frame, 
            text="Resumen académico y operativo", 
            font=ctk.CTkFont(size=13),
            text_color=COLOR_PALETTE["text_secondary"]
        )
        self.section_subtitle.pack(anchor="w")
        
        # Buscador
        self.search_entry = ctk.CTkEntry(
            self,
            placeholder_text="🔍 Buscar estudiante...",
            width=300,
            height=40,
            corner_radius=20,
            fg_color=COLOR_PALETTE["bg_card"],
            border_color=COLOR_PALETTE["border"],
            border_width=1,
            text_color=COLOR_PALETTE["text_primary"]
        )
        self.search_entry.grid(row=0, column=1, pady=20)
        
        # Perfil y Notificaciones
        self.right_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.right_frame.grid(row=0, column=2, padx=30, pady=20, sticky="e")
        
        self.notif_btn = ctk.CTkButton(
            self.right_frame,
            text="🔔",
            width=40, height=40, corner_radius=20,
            fg_color=COLOR_PALETTE["bg_card"],
            text_color=COLOR_PALETTE["red"],
            hover_color=COLOR_PALETTE["border"],
            border_width=1, border_color=COLOR_PALETTE["border"]
        )
        self.notif_btn.pack(side="left", padx=(0, 20))
        
        # Avatar
        self.avatar_frame = ctk.CTkFrame(self.right_frame, width=40, height=40, corner_radius=20, fg_color=COLOR_PALETTE["blue"])
        self.avatar_frame.pack(side="left")
        self.avatar_frame.pack_propagate(False)
        
        # Usar las 2 primeras letras del nombre de usuario
        initials = user_name[:2].upper() if user_name else "AD"
        self.avatar_lbl = ctk.CTkLabel(self.avatar_frame, text=initials, text_color="white", font=ctk.CTkFont(weight="bold"))
        self.avatar_lbl.place(relx=0.5, rely=0.5, anchor="center")
        
        # Info usuario
        self.user_text_frame = ctk.CTkFrame(self.right_frame, fg_color="transparent")
        self.user_text_frame.pack(side="left", padx=10)
        
        self.user_name_lbl = ctk.CTkLabel(
            self.user_text_frame, text=user_name, font=ctk.CTkFont(size=14, weight="bold"), text_color=COLOR_PALETTE["text_primary"]
        )
        self.user_name_lbl.pack(anchor="w")
        self.user_role_lbl = ctk.CTkLabel(
            self.user_text_frame, text="Coordinador", font=ctk.CTkFont(size=12), text_color=COLOR_PALETTE["text_secondary"]
        )
        self.user_role_lbl.pack(anchor="w")

    def set_section(self, title: str):
        self.section_title.configure(text=title)
        if title == "Dashboard":
            self.section_subtitle.configure(text="Resumen académico y operativo")
            self.section_title.configure(text="Vista General")
        else:
            self.section_subtitle.configure(text=f"Gestión de {title.lower()}")
