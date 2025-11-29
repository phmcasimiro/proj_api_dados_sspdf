# services.py
# Autor: Pedro Casimiro
# Data: 26/11/2025

import pandas as pd
import logging
from src.config import PathConfig

# Cria um logger com o nome do módulo ('src.services.services')
# Este logger será configurado globalmente no main.py
logger = logging.getLogger(__name__)


# --------------------------------------------------------------------------
# Classe de Serviço
# --------------------------------------------------------------------------

"""
Camada de Serviço responsável por carregar e fornecer consultas
ao DataFrame consolidado de ocorrências. O DF é carregado na memória
apenas uma vez para garantir a performance da API.
"""


class OcorrenciasService:  # Indica que a classe pertence ao módulo 'src.services.services'

    df: pd.DataFrame = (
        None  # Variável de classe que armazenará o DataFrame (carregamento único)
    )

    @classmethod  # Indica que o método é um método de classe

    # Carregar DataFrame consolidado na memória, se ainda não estiver carregado.
    def load_data(cls):
        if cls.df is None:

            # Log de início do carregamento
            logger.info(
                f"Iniciando carregamento do DF consolidado de: {PathConfig.PATH_FINAL_DF.as_posix()}"
            )

            # Tentativa de carregar o DataFrame
            try:
                # O método lê o arquivo que foi salvo pelo pipeline_etl.py
                cls.df = pd.read_csv(
                    PathConfig.PATH_FINAL_DF.as_posix(), sep=";", encoding="utf-8"
                )
                # Log de sucesso do carregamento
                logger.info(
                    f"DF consolidado carregado com sucesso! Linhas: {len(cls.df)}"
                )

            # Tratamento de erro
            except FileNotFoundError:
                # Registra o erro no log
                logger.error(
                    f"Arquivo de dados não encontrado em: {PathConfig.PATH_FINAL_DF.as_posix()}. "
                    "Execute 'python -m src.data.pipeline_etl' primeiro.",
                    exc_info=True,  # Adiciona o stack trace completo ao log do arquivo
                )
                # Lança o erro para que possa ser tratado pelo orchestrador (main.py)
                raise FileNotFoundError(
                    f"Arquivo de dados não encontrado em: {PathConfig.PATH_FINAL_DF.as_posix()}. "
                    "Execute 'python -m src.data.pipeline_etl' primeiro."
                )

    @classmethod  # Indica que o método é um método de classe
    # Indica que o método retorna uma lista de dicionários (formato JSON ideal para APIs).
    def get_all_data(
        cls,
    ) -> list[dict]:

        # Garantir que os dados estão carregados na memória
        if cls.df is None:
            cls.load_data()

        # Retornar DF em memória convertido para uma lista de dicionários
        return cls.df.to_dict(orient="records")


'''
    # Exemplo futuro: método para filtrar os dados
    @classmethod
    def filter_by_ra(cls, regiao_administrativa: str) -> list[dict]:
        """Filtra as ocorrências por Região Administrativa (case-insensitive)."""
        if cls.df is None:
            cls.load_data()

        # Cria uma máscara booleana para filtrar o DataFrame em memória
        mask = (
            cls.df["RegiaoAdministrativa"].str.lower() == regiao_administrativa.lower()
        )

        return cls.df[mask].to_dict(orient="records")
'''
