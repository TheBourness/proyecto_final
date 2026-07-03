import os
from pathlib import Path

# Base directory paths
BASE_DIR = Path(__file__).resolve().parent
DATABASE_DIR = BASE_DIR / "database"
DATABASE_DIR.mkdir(exist_ok=True)

# Database configuration
DATABASE_URL = f"sqlite:///{DATABASE_DIR}/becatrack.db"

# Storage Directories
ASSETS_DIR = BASE_DIR / "assets"
ICONS_DIR = ASSETS_DIR / "icons"
IMAGES_DIR = ASSETS_DIR / "images"

REPORTS_DIR = BASE_DIR / "reports"
REPORTS_DIR.mkdir(exist_ok=True)

# App Configuration
APP_TITLE = "BecaTrack - Gestión de Becarios"
APP_RESOLUTION = "1200x900"
APP_MIN_RESOLUTION = "1024x768"

# UI Theme & Colors (Tema Claro Moderno - Inspirado en Web)
COLOR_PALETTE = {
    "bg_app": "#F9FAFB",         # Gris muy claro para el fondo principal
    "bg_card": "#FFFFFF",        # Blanco puro para tarjetas
    "blue": "#3B82F6",           # Azul brillante
    "blue_light": "#EFF6FF",     # Fondo azul pastel para botones activos
    "green": "#10B981",          # Verde esmeralda
    "green_light": "#ECFDF5",    # Fondo verde suave
    "red": "#EF4444",            # Rojo coral
    "red_light": "#FEF2F2",      # Fondo rojo suave
    "text_primary": "#111827",   # Gris muy oscuro
    "text_secondary": "#6B7280", # Gris medio
    "border": "#E5E7EB",         # Gris clarito para bordes sutiles
    "sidebar_bg": "#FFFFFF",     # Blanco puro para la barra lateral
    # Alias de compatibilidad para pantallas antiguas:
    "black": "#F9FAFB",          # Ahora mapea al fondo claro
    "dark_gray": "#FFFFFF",      # Ahora mapea al fondo de tarjeta blanco
    "gray": "#E5E7EB"
}
