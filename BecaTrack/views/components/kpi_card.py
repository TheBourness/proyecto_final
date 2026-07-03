import customtkinter as ctk
from config import COLOR_PALETTE

class KPICard(ctk.CTkFrame):
    """Tarjeta moderna blanca con subtítulo e icono encapsulado."""
    def __init__(self, parent, title: str, value: str, subtitle: str = "", icon: str = "", bg_icon_color: str = COLOR_PALETTE["blue_light"], icon_color: str = COLOR_PALETTE["blue"]):
        super().__init__(
            parent, 
            fg_color=COLOR_PALETTE["bg_card"], 
            corner_radius=15,
            border_width=1,
            border_color=COLOR_PALETTE["border"]
        )
        
        self.grid_propagate(False)
        self.configure(width=280, height=140)
        
        self.title_label = ctk.CTkLabel(
            self, 
            text=title, 
            font=ctk.CTkFont(size=13, weight="normal"),
            text_color=COLOR_PALETTE["text_secondary"]
        )
        self.title_label.place(relx=0.08, rely=0.15)
        
        self.value_label = ctk.CTkLabel(
            self,
            text=str(value),
            font=ctk.CTkFont(family="Inter", size=36, weight="bold"),
            text_color=COLOR_PALETTE["text_primary"]
        )
        self.value_label.place(relx=0.08, rely=0.35)
        
        self.subtitle_label = ctk.CTkLabel(
            self,
            text=subtitle,
            font=ctk.CTkFont(size=11),
            text_color=COLOR_PALETTE["green"] if "↑" in subtitle or "Estable" in subtitle else COLOR_PALETTE["text_secondary"]
        )
        self.subtitle_label.place(relx=0.08, rely=0.7)
        
        if icon:
            self.icon_frame = ctk.CTkFrame(
                self, 
                width=45, height=45, 
                corner_radius=12, 
                fg_color=bg_icon_color
            )
            self.icon_frame.place(relx=0.8, rely=0.15)
            self.icon_frame.pack_propagate(False)
            
            self.icon_label = ctk.CTkLabel(
                self.icon_frame,
                text=icon,
                font=ctk.CTkFont(size=22),
                text_color=icon_color
            )
            self.icon_label.place(relx=0.5, rely=0.5, anchor="center")
            
    def update_value(self, new_value: str):
        self.value_label.configure(text=str(new_value))
