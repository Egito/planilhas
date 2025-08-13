from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class Tema(Base):
    __tablename__ = "temas"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), unique=True, index=True)
    peso = Column(Float, nullable=False)
    descricao = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relacionamentos
    perguntas = relationship("Pergunta", back_populates="tema")
    avaliacoes = relationship("Avaliacao", back_populates="tema")
