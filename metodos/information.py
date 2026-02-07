import pandas as pd
import math
from pandas import DataFrame
from scipy.stats import norm

from igraph import IGraph


class Information(IGraph):

    @staticmethod
    def show(df: DataFrame, **kwargs):
        ref = kwargs.get("ref")
        numero_observacoes = df[kwargs.get("coluna")].count()
        valor_max = df[kwargs.get("coluna")].max()
        valor_min = df[kwargs.get("coluna")].min()
        media = df[kwargs.get("coluna")].mean()
        desvio_padrao = df[kwargs.get("coluna")].std()

        # Visao geral
        print('')
        print(f'> Analise: [{kwargs.get("coluna")}]')

        print('\n')
        print(f'> Observações: {numero_observacoes}')
        print(f'> Max.: {valor_max}')
        print(f'> Min.: {valor_min}')
        print(f'> Média: {media:.4f}')
        print(f'> Desvio padrão: {desvio_padrao:.4f}')
        print('\n')

        # Probabilidade
        print(f'> Probabilidade de x > {ref}')
        probabilidade = norm.sf(ref, loc=media, scale=desvio_padrao)
        print(f'{probabilidade:.4f} ({1-probabilidade:.4f})')
        print('\n')

        # Produtos
        unique_prod = pd.DataFrame(df["descr.produto"].unique(), columns=['Descr.produto'])
        # unique_prod['Produto'] = df["produto"].unique()

        count_prod = []
        for prod in unique_prod["Descr.produto"]:
            count_prod.append(df["descr.produto"].value_counts().get(prod, 0))
        unique_prod["Counts"] = count_prod

        unique_prod = unique_prod.sort_values(by="Counts", ascending=False)
        print(f'> Produtos\n{unique_prod.head(20)}')

