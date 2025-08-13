from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.temas import router as temas_router
from config.database import engine
import models
from models.base import Base

# Criar tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Inicializar aplicação FastAPI
app = FastAPI(
    title="Sistema IDF",
    description="API para Sistema de Indicador de Desempenho de Fornecedor",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rotas
app.include_router(temas_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
