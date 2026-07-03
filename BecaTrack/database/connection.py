from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
import os

# Asegurar que la ruta base esté en el PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import DATABASE_URL
from models.base import Base

# Importar todos los modelos para que SQLAlchemy los reconozca al crear las tablas
import models.user
import models.student
import models.monitor
import models.tracking

# Inicializar motor de base de datos
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
    """Retorna una nueva sesión de la base de datos."""
    return SessionLocal()

def init_db():
    """Crea todas las tablas en la base de datos si no existen."""
    Base.metadata.create_all(bind=engine)
