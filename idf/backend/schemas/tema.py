from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class TemaBase(BaseModel):
    nome: str
    peso: float
    descricao: Optional[str] = None


class TemaCreate(TemaBase):
    pass


class TemaResponse(TemaBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class Tema(TemaBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
