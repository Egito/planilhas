from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base
from .pergunta import TipoResposta


class Resposta(Base):
    __tablename__ = "respostas"
    
    id = Column(Integer, primary_key=True, index=True)
    avaliacao_id = Column(Integer, ForeignKey("avaliacoes.id"))
    pergunta_id = Column(Integer, ForeignKey("perguntas.id"))
    valor = Column(Enum(TipoResposta), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relacionamentos
    avaliacao = relationship("Avaliacao", back_populates="respostas")
    pergunta = relationship("Pergunta", back_populates="respostas")
