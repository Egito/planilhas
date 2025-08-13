from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from models import Tema
from schemas.tema import TemaCreate, TemaResponse
from config.database import get_db

router = APIRouter(prefix="/temas", tags=["temas"])

@router.post("/", response_model=TemaResponse)
def criar_tema(tema: TemaCreate, db: Session = Depends(get_db)):
    db_tema = Tema(**tema.dict())
    db.add(db_tema)
    db.commit()
    db.refresh(db_tema)
    return db_tema

@router.get("/", response_model=List[TemaResponse])
def listar_temas(db: Session = Depends(get_db)):
    return db.query(Tema).all()
