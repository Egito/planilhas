from sqlalchemy import Column, Integer, String, Enum, DateTime
from datetime import datetime
from .base import Base
import enum


class PerfilUsuario(enum.Enum):
    FISCAL_CAMPO = "fiscal_campo"
    FISCAL_ADMINISTRATIVO = "fiscal_administrativo"
    GERENTE = "gerente"


class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True)
    senha_hash = Column(String(100), nullable=False)
    perfil = Column(Enum(PerfilUsuario), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
