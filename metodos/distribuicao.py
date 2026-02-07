import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame

from igraph import IGraph


class Distribuicao(IGraph):

    @staticmethod
    def show(df: DataFrame, **kwargs):
        analise = kwargs.get('coluna')
        produto = kwargs.get('produto')
        loc = kwargs.get('loc')
        ref = kwargs.get('ref')

        df_copy = df.copy()
        df_copy['ref'] = ref

        fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

        sns.stripplot(data=df_copy[analise], log_scale=False, jitter=True, size=6, orient='v', ax=ax1)
        sns.stripplot(data=df_copy['ref'], log_scale=False, jitter=False, size=6, orient='v', ax=ax1,
                      label='{:.2f}'.format(ref))
        ax1.grid(color='k', linestyle=':', linewidth=1, alpha=.2)
        ax1.set_title('Análise: {}\nloc:{} / código: {}'.format(analise, loc, produto), loc='left', fontsize=9)
        ax1.legend(loc='upper right', fontsize=9)

        ax2.boxplot(df_copy[analise])

        sns.histplot(data=df_copy[analise], kde=True, element="step", ax=ax3)
        ax3.axvline(x=ref, color='red', linestyle='-.', linewidth=1, label='ref.:{:.0f}'.format(ref))
        ax3.grid(color='k', linestyle=':', linewidth=1, alpha=.2)

        plt.show()
