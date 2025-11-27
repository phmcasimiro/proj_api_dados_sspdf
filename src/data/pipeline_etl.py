# pipeline_etl.py

import pandas as pd
from src.config import PathConfig
import logging
from src.config import setup_logging

# Logger global
logger = logging.getLogger(__name__)


def criar_df_consolidado() -> pd.DataFrame:
    """
    Realiza o ETL: Extrai, transforma (junta) e retorna o DataFrame consolidado,
    usando os caminhos definidos em PathConfig.
    """

    # 1. EXTRAÇÃO (E)
    print("Iniciando Extração dos dados...")
    df_principal = pd.read_csv(PathConfig.PATH_PRINCIPAL_CSV.as_posix(), sep=";")
    df_natureza = pd.read_csv(PathConfig.PATH_NATUREZA_CSV.as_posix(), sep=";")
    df_ra = pd.read_csv(PathConfig.PATH_RA_CSV.as_posix(), sep=";")

    # 2. TRANSFORMAÇÃO (T)
    print("Iniciando Junção (Merge) dos dados...")

    # Prepara DF de Natureza
    df_natureza = df_natureza[["cod_natureza", "natureza"]].copy()

    # Prepara DF de RA
    df_ra = df_ra[["id_ra", "RegiaoAdministrativa"]].copy()

    # 2.1. Primeira Junção (Natureza)
    df_temp = pd.merge(df_principal, df_natureza, on="cod_natureza", how="left")

    # 2.2. Segunda Junção (Região Administrativa)
    df_consolidado = pd.merge(df_temp, df_ra, on="id_ra", how="left")

    # 2.3. Limpeza e Finalização
    df_consolidado["quantidade"] = df_consolidado["quantidade"].fillna(0).astype(int)
    df_consolidado.drop(columns=["cod_natureza", "id_ra"], inplace=True)

    # Reordenando as colunas
    df_consolidado = df_consolidado[
        ["id", "mes", "ano", "RegiaoAdministrativa", "natureza", "quantidade"]
    ].copy()

    print("DataFrame Consolidado criado com sucesso!")
    return df_consolidado


# O bloco principal deve aparecer APENAS UMA VEZ e estar limpo.
if __name__ == "__main__":
    print("--- Executando Pipeline ETL ---")

    # Chamando a função sem passar caminhos!
    df_final = criar_df_consolidado()

    # 3. CARGA (L) - Salvando o arquivo final no caminho definido
    df_final.to_csv(PathConfig.PATH_FINAL_DF.as_posix(), index=False, sep=";")

    print(f"\nDataFrame salvo com sucesso em: {PathConfig.PATH_FINAL_DF.as_posix()}")
    print("\nVisualização das primeiras 5 linhas do DF consolidado:")
    print(df_final.head())
    print("\n--- Pipeline ETL Finalizado ---")
