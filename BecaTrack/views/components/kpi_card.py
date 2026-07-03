import customtkinter as ctk
from config import COLOR_PALETTE

class KPICard(ctk.CTkFrame):
    """Tarjeta para mostrar un KPI (Key Performance Indicator) en el Dashboard."""
    
    def __init__(self, parent, title: str, value: str, icon: str = "", color: str = COLOR_PALETTE["blue"]):
        super().__init__(parent, fg_color=COLOR_PALETTE["dark_gray"], corner_radius=10)
        
        self.grid_propagate(False)
        self.configure(width=220, height=120)
        
        # Barra de color indicadora a la izquierda
        self.color_bar = ctk.CTkFrame(self, width=6, corner_radius=0, fg_color=color)
        self.color_bar.place(relx=0, rely=0, relwidth=0.03, relheight=1.0)
        
        # Título
        self.title_label = ctk.CTkLabel(
            self, 
            text=title, 
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=COLOR_PALETTE["text_secondary"]
        )
        self.title_label.place(relx=0.1, rely=0.15)
        
        # Valor
        self.value_label = ctk.CTkLabel(
            self,
            text=str(value),
            font=ctk.CTkFont(family="Inter", size=32, weight="bold"),
            text_color=COLOR_PALETTE["text_primary"]
        )
        self.value_label.place(relx=0.1, rely=0.45)
        
        # Icono de texto
        if icon:
            self.icon_label = ctk.CTkLabel(
                self,
                text=icon,
                font=ctk.CTkFont(size=36),
                text_color=color
            )
            self.icon_label.place(relx=0.75, rely=0.35)
            
    def update_value(self, new_value: str):
        self.value_label.configure(text=str(new_value))
