# config.py
# Arquivo de configuração do projeto
# Autor: Pedro Casimiro
# Data: 26/11/2025

import os
from pathlib import Path

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
