from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base
import enum


class TipoResposta(enum.Enum):
    ATENDEU_100 = 100
    ATENDEU_80_95 = 87.5
    ATENDEU_60_79 = 69.5
    NAO_ATENDEU = 0
    NAO_APLICAVEL = None


class Pergunta(Base):
    __tablename__ = "perguntas"
    
    id = Column(Integer, primary_key=True, index=True)
    texto = Column(String(500), nullable=False)
    tema_id = Column(Integer, ForeignKey("temas.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relacionamentos
    tema = relationship("Tema", back_populates="perguntas")
    respostas = relationship("Resposta", back_populates="pergunta")
