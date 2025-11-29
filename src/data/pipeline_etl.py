# pipeline_etl.py
# Autor: Pedro Casimiro
# Data: 26/11/2025

import pandas as pd
from src.config import PathConfig
import logging
from src.config import setup_logging

# Logger global
logger = logging.getLogger(__name__)


# ETL: Extrai, transforma (junta) e retorna o DataFrame consolidado
# Usa caminhos definidos em PathConfig.
def criar_df_consolidado() -> pd.DataFrame:
    # 1. EXTRAÇÃO (E)
    # Log de início da extração (boa prática)
    logger.info("Iniciando Extração dos dados...")
    # Log de rastreio de caminhos (boa prática)
    logger.info(
        f"Lendo dados principais de: {PathConfig.PATH_PRINCIPAL_CSV.as_posix()}"
    )
    # Leitura dos arquivos CSV
    df_principal = pd.read_csv(PathConfig.PATH_PRINCIPAL_CSV.as_posix(), sep=";")
    df_natureza = pd.read_csv(PathConfig.PATH_NATUREZA_CSV.as_posix(), sep=";")
    df_ra = pd.read_csv(PathConfig.PATH_RA_CSV.as_posix(), sep=";")

    # 2. TRANSFORMAÇÃO (T)

    # Log de início da transformação
    logger.info("Iniciando Junção (Merge) dos dados...")

    # Prepara DF de Natureza
    df_natureza = df_natureza[["cod_natureza", "natureza"]].copy()

    # Prepara DF de RA
    df_ra = df_ra[["id_ra", "RegiaoAdministrativa"]].copy()

    # 2.1. Primeira Junção (Natureza)
    df_temp = pd.merge(df_principal, df_natureza, on="cod_natureza", how="left")

    # 2.2. Segunda Junção (Região Administrativa)
    df_consolidado = pd.merge(df_temp, df_ra, on="id_ra", how="left")

    # 2.3. Limpeza e Finalização
    # Preencher valores nulos com 0 e converte para int
    df_consolidado["quantidade"] = df_consolidado["quantidade"].fillna(0).astype(int)
    # Remover colunas desnecessárias
    df_consolidado.drop(columns=["cod_natureza", "id_ra"], inplace=True)

    # Reordenar as colunas
    df_consolidado = df_consolidado[
        ["id", "mes", "ano", "RegiaoAdministrativa", "natureza", "quantidade"]
    ].copy()

    # Log de sucesso na transformação
    logger.info("DataFrame Consolidado criado com sucesso!")
    return df_consolidado


# Ponto de Entrada do Script
# Função: Garantir que o script seja executado quando for chamado diretamente
# Função: Executar o pipeline ETL
# Função: Proteger das importações
# Função: Executar o pipeline ETL
if __name__ == "__main__":

    # 1. ATIVAÇÃO: Chamar função de inicialização do logging
    setup_logging()
    logger.info("--- Executando Pipeline ETL ---")

    try:
        # Chamar a função "criar_df_consolidado()"
        df_final = criar_df_consolidado()

        # 3. CARGA (L) - Salvar o arquivo final no caminho definido
        # Log de início da carga
        logger.info(
            f"Salvando DataFrame final em: {PathConfig.PATH_FINAL_DF.as_posix()}"
        )
        # Salvar o arquivo final no caminho definido
        df_final.to_csv(PathConfig.PATH_FINAL_DF.as_posix(), index=False, sep=";")

        # Log de sucesso na carga
        logger.info(f"DataFrame salvo com sucesso! Total de linhas: {len(df_final)}")

        # print() para exibição tabular
        print("\nVisualização das primeiras 5 linhas do DF consolidado:")
        print(df_final.head())

        # Log de finalização
        logger.info("--- Pipeline ETL Finalizado ---")

    except Exception as e:
        # Adicionar tratamento de exceção para logs de erro
        logger.exception("ERRO CRÍTICO ao executar o pipeline ETL.")
