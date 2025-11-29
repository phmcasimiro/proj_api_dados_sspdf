# config.py
# Arquivo de configuração do projeto
# Autor: Pedro Casimiro
# Data: 26/11/2025

import os
from pathlib import Path
import logging

# --------------------------------------------------------------------------
# Configurações Gerais da API
# --------------------------------------------------------------------------

# Configurações gerais da API
API_VERSION = "1.0.0"
API_TITLE = "API Ocorrências SSP-DF"
API_DESCRIPTION = "API para servir dados de ocorrências policiais SSP-DF"

# --------------------------------------------------------------------------
# Configurações de Logging
# --------------------------------------------------------------------------

# Níveis logging (INFO, DEBUG, WARNING, ERROR, CRITICAL)
LOG_LEVEL = logging.INFO
# Formato do log
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
# Diretório de logs
LOG_DIR = Path("logs")
# Criar diretório de logs se não existir
LOG_DIR.mkdir(exist_ok=True)


# Configurar sistema de logging da aplicação
def setup_logging():
    logging.basicConfig(
        # Nível de logging
        level=LOG_LEVEL,
        # Formato do log
        format=LOG_FORMAT,
        # Handlers
        handlers=[logging.FileHandler(LOG_DIR / "app.log"), logging.StreamHandler()],
    )
    # Logger Global para uso em outros módulos
    return logging.getLogger("api_sspdf")


# Logger Global para uso em outros módulos
# Variável inicializada por demanda
logger = logging.getLogger("api_sspdf")


# --------------------------------------------------------------------------
# Configurações da Raiz do Projeto
# --------------------------------------------------------------------------

# Define o caminho raiz do projeto para que todos os caminhos relativos funcionem
# A função Path(__file__).resolve().parent sobe para 'proj_api_dados_sspdf/'
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# --------------------------------------------------------------------------
# Definição dos Caminhos de Dados e Artefatos
# --------------------------------------------------------------------------


class PathConfig:
    """Configurações de Caminhos para o Projeto."""

    # Pasta Base dos Dados Brutos (src/data/)
    DATA_DIR = PROJECT_ROOT / "src" / "data"

    # Caminhos para os arquivos CSV de entrada
    PATH_PRINCIPAL_CSV = DATA_DIR / "ocorrencias_consolidado_2020_24.csv"
    PATH_NATUREZA_CSV = DATA_DIR / "ocorrencias_natureza.csv"
    PATH_RA_CSV = DATA_DIR / "ocorrencias_ra.csv"

    # Pasta onde os dados processados serão salvos (implementando sua sugestão)
    PROCESSED_DATA_DIR = DATA_DIR / "processed"

    # Caminho onde o arquivo final consolidado será salvo
    PATH_FINAL_DF = PROCESSED_DATA_DIR / "ocorrencias_final.csv"


# --------------------------------------------------------------------------
# Definição de Variáveis de Ambiente e Outras Configs (Ex: ML)
# --------------------------------------------------------------------------


class AppConfig:
    """Configurações gerais da aplicação (API, ML, etc.)."""

    # Exemplo: Chave de ambiente para o modo da aplicação
    APP_ENV = os.getenv("APP_ENV", "development")

    # Exemplo: Parâmetros do modelo (se fosse um projeto mais avançado)
    ML_MODEL_VERSION = "v1.0"
