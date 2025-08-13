# models.py
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy import Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func # Para created_at/updated_at
from database import Base

class BaseTable(Base):
    id = Column(Integer, primary_key=True)
    created_at = Column(Datetime, default=now())
    modified_at = Column(Datetime, default=now())
    deleted_at = Column(Datetime)

class Usuario(BaseTable):
    __tablename__ = 'usuarios'
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    tarefas = relationship('Tarefa', back_populates='usuario')

class Tarefa(BaseTable):
    __tablename__ = 'tarefas'
    descricao = Column(String, nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuario = relationship('Usuario', back_populates='tarefas')

class Pce_Tipol(BaseTable):
    __tablename__ = 'pce_tipols'
    descricao = Column(String, nullable=False)

class Pce_ItemPPU(BaseTable):
    __tablename__ = 'pce_itemppus'
    descricao = Column(String, nullable=False)

class Pce_Local(BaseTable):
    __tablename__ = 'pce_locals'
    descricao = Column(String, nullable=False)

class Pce_Partnum(BaseTable):
    __tablename__ = 'pce_partnums'
    codigo = Column(String, nullable=False)
    descricao = Column(String, nullable=False)

class Pce_Prod(BaseTable):
    __tablename__ = 'pce_prods'
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    partnum_id = Column(Integer, ForeignKey('pce_partnums.id'))
    tipol_id = Column(Integer, ForeignKey('pce_tipols.id'))

    usuario = relationship('Usuario', back_populates='pce_prods')
    partnum = relationship('Pce_Partnum', back_populates='pce_prods')
    tipol = relationship('Pce_Tipol', back_populates='pce_prods')
    
    serial = Column(String, nullable=False)
    ativo = Column(String, nullable=True)

class Pce_Movim(BaseTable):
    __tablename__ = 'pce_movims'
    pce_prod_id = Column(Integer, ForeignKey('pce_prods.id'))
    pce_tipol_id = Column(Integer, ForeignKey('pce_tipols.id'))
    pce_itemppu_id = Column(Integer, ForeignKey('pce_itemppus.id'))
    pce_local_id = Column(Integer, ForeignKey('pce_locals.id'))
    
    prod = relationship('Pce_Prod', back_populates='pce_movims')
    tipol = relationship('Pce_Tipol', back_populates='pce_movims')
    itemppu = relationship('Pce_ItemPPU', back_populates='pce_movims')
    local = relationship('Pce_Local', back_populates='pce_movims')

    nfe = Column(String, nullable=True)
    serial = Column(Float, nullable=False)
    emissao = Column(Datetime, nullable=False)
    cliente = Column(String, nullable=False)
    municipio = Column(String, nullable=False)
    uf = Column(String, nullable=False)
    solic_num = Column(String, nullable=False)
    dt_movim = Column(Datetime, nullable=False)


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    nome = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relação com Acessos (um usuário pode ter muitos acessos)
    acessos = relationship("Acesso", back_populates="usuario")

class Aplicacao(Base):
    __tablename__ = "aplicacoes" # Usado "aplicacoes" para evitar conflito com palavra reservada 'application' em alguns DBs

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True, nullable=False)
    slug = Column(String, unique=True, index=True, nullable=False) # Ex: 'app_vendas', 'app_rh'

    # Relação com Transacoes (uma aplicação pode ter muitas transações)
    transacoes = relationship("Transacao", back_populates="aplicacao")

class Transacao(Base):
    __tablename__ = "transacoes"

    id = Column(Integer, primary_key=True, index=True)
    aplicacao_id = Column(Integer, ForeignKey("aplicacoes.id"), nullable=False)
    nome = Column(String, nullable=False) # Ex: 'Cadastrar Cliente', 'Emitir Nota'
    slug = Column(String, nullable=False) # Ex: 'cad_cliente', 'emitir_nota'

    # Relações
    aplicacao = relationship("Aplicacao", back_populates="transacoes")
    acessos = relationship("Acesso", back_populates="transacao")

    # Garante que 'slug' seja único dentro de uma 'aplicacao_id'
    __table_args__ = (UniqueConstraint('aplicacao_id', 'slug', name='_aplicacao_slug_uc'),)


class Acesso(Base):
    __tablename__ = "acessos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    transacao_id = Column(Integer, ForeignKey("transacoes.id"), nullable=False)
    # Coluna 'default' renomeada para 'acesso_padrao' para evitar conflito com palavra reservada
    acesso_padrao = Column(Boolean, default=False, nullable=False) # default {sim/nao}

    # Relações
    usuario = relationship("Usuario", back_populates="acessos")
    transacao = relationship("Transacao", back_populates="acessos")

    # Garante que cada par usuario-transacao seja único
    __table_args__ = (UniqueConstraint('usuario_id', 'transacao_id', name='_usuario_transacao_uc'),)

# O modelo Item original foi removido para focar no seu novo esquema.
# Se precisar dele, pode adicioná-lo de volta.
# class Item(Base):
#     __tablename__ = "items"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     description = Column(String, nullable=True)
#     is_active = Column(Boolean, default=True)

Session = init_db()