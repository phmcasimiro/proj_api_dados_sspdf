# main.py (Versão Ajustada)

from fastapi import FastAPI

# Importamos a função de setup e o logger que será configurado
from src.config import API_VERSION, API_TITLE, API_DESCRIPTION, setup_logging
from src.services.services import OcorrenciasService  # Inicialização dos dados

# 1. Configurar o Logging no ponto de entrada
logger = setup_logging()

# 2. Configurar a aplicação FastAPI
app = FastAPI(title=API_TITLE, description=API_DESCRIPTION, version=API_VERSION)


# 3. Carregar os dados na memória no início da aplicação
@app.on_event("startup")
def startup_event():
    """
    Função executada quando a API inicia.
    Usada para carregar o DataFrame na memória.
    """
    logger.info("Iniciando a API. Carregando dados na memória...")
    OcorrenciasService.load_data()
    logger.info("Dados de ocorrências carregados com sucesso!")


# --- Endpoints ---


@app.get("/")
def root():
    """
    Endpoint raiz da API
    """
    # Usando o logger configurado
    logger.info("Endpoint raiz acessado")
    return {"message": "API de Dados está funcionando!", "version": API_VERSION}


@app.get("/health")
def health_check():
    """
    Endpoint de health check
    """
    # Usando o logger configurado
    logger.debug("Health check realizado")  # Nível DEBUG para não poluir o INFO
    return {"status": "healthy", "version": API_VERSION}
