# services.py
# Autor: Pedro Casimiro
# Data: 26/11/2025

import pandas as pd
from src.config import PathConfig

class OcorrenciasService:
    """
    Camada de Serviço responsável por carregar e fornecer consultas
    ao DataFrame consolidado de ocorrências. O DF é carregado na memória
    apenas uma vez para garantir a performance da API.
    """
    
    # Variável de classe que armazenará o DataFrame (carregamento único)
    df: pd.DataFrame = None

    @classmethod
    def load_data(cls):
        """Carrega o DataFrame consolidado na memória, se ainda não estiver carregado."""
        if cls.df is None:
            print(f"[{__name__}] - Carregando DF consolidado de: {PathConfig.PATH_FINAL_DF.as_posix()}")
            try:
                # O método lê o arquivo que foi salvo pelo pipeline_etl.py
                cls.df = pd.read_csv(
                    PathConfig.PATH_FINAL_DF.as_posix(),
                    sep=';'
                )
                print(f"[{__name__}] - DF consolidado carregado com sucesso! Linhas: {len(cls.df)}")
            except FileNotFoundError:
                raise FileNotFoundError(
                    f"Arquivo de dados não encontrado em: {PathConfig.PATH_FINAL_DF.as_posix()}. "
                    "Execute 'python -m src.data.pipeline_etl' primeiro."
                )

    @classmethod
    def get_all_data(cls) -> list[dict]:
        """
        Retorna todos os registros do DataFrame como uma lista de dicionários
        (formato JSON ideal para APIs).
        """
        # Garante que os dados estão carregados na memória
        if cls.df is None:
            cls.load_data()
            
        # Retorna o DF em memória convertido para uma lista de dicionários
        return cls.df.to_dict(orient='records')

    # Exemplo futuro: método para filtrar os dados
    @classmethod
    def filter_by_ra(cls, regiao_administrativa: str) -> list[dict]:
        """Filtra as ocorrências por Região Administrativa (case-insensitive)."""
        if cls.df is None:
            cls.load_data()

        # Cria uma máscara booleana para filtrar o DataFrame em memória
        mask = cls.df['RegiaoAdministrativa'].str.lower() == regiao_administrativa.lower()
        
        return cls.df[mask].to_dict(orient='records')