from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class Avaliacao(Base):
    __tablename__ = "avaliacoes"
    
    id = Column(Integer, primary_key=True, index=True)
    fornecedor_id = Column(Integer, ForeignKey("fornecedores.id"))
    avaliador_id = Column(Integer, ForeignKey("usuarios.id"))
    tema_id = Column(Integer, ForeignKey("temas.id"))
    periodo = Column(String(50), nullable=False)  # Ex: "2025-08"
    nota_final = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relacionamentos
    fornecedor = relationship("Fornecedor", back_populates="avaliacoes")
    avaliador = relationship("Usuario", back_populates="avaliacoes")
    tema = relationship("Tema", back_populates="avaliacoes")
    respostas = relationship("Resposta", back_populates="avaliacao")
