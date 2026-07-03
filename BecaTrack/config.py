import os
from pathlib import Path

# Base directory paths
BASE_DIR = Path(__file__).resolve().parent
DATABASE_DIR = BASE_DIR / "database"
DATABASE_DIR.mkdir(exist_ok=True)

# Database configuration
# Using SQLite as requested
DATABASE_URL = f"sqlite:///{DATABASE_DIR}/becatrack.db"

# Storage Directories
ASSETS_DIR = BASE_DIR / "assets"
ICONS_DIR = ASSETS_DIR / "icons"
IMAGES_DIR = ASSETS_DIR / "images"

REPORTS_DIR = BASE_DIR / "reports"
REPORTS_DIR.mkdir(exist_ok=True)

# App Configuration
APP_TITLE = "BecaTrack - Gestión de Becarios"
APP_RESOLUTION = "1200x800"
APP_MIN_RESOLUTION = "1024x768"

# UI Theme & Colors (As requested)
COLOR_PALETTE = {
    "blue": "#2563EB",
    "dark_gray": "#1F2937",
    "black": "#111827",
    "green": "#22C55E",
    "red": "#EF4444",
    "text_primary": "#F9FAFB",
    "text_secondary": "#9CA3AF",
    "border": "#374151"
}
