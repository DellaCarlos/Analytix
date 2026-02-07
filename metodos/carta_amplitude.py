from itertools import tee
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame

from igraph import IGraph



class CartaControleAmplitude(IGraph):

    @staticmethod
    def show(df: DataFrame, **kwargs):
        analise = kwargs.get('coluna')
        produto = kwargs.get('produto')
        loc = kwargs.get('loc')
        ref = kwargs.get('ref')

        df_copy = df.copy()

        mean = np.mean(df_copy[analise])
        df_copy['lcc'] = mean
        limits = CartaControleAmplitude.control_limts_definition(df_copy[analise], mean)
        df_copy['lcs'] = limits[0]
        df_copy['lci'] = limits[1]

        df_copy['index'] = np.arange(1, len(df_copy[analise]) + 1)

        plt.plot(df_copy['index'], df_copy[analise], '.-')
        plt.plot(df_copy['index'], df_copy['lcs'], 'k--', label='LCS = {:.3f}'.format(limits[0]), alpha=0.7)
        plt.plot(df_copy['index'], df_copy['lcc'], 'r-', label='LCC = {:.3f}'.format(mean), alpha=0.3)
        plt.plot(df_copy['index'], df_copy['lci'], 'k--', label='LCS = {:.3f}'.format(limits[1]), alpha=0.7)
        plt.grid(color='k', linestyle=':', linewidth=1, alpha=.2)
        plt.title('Análise: {}\nloc:{} / código: {}'.format(analise, loc, produto), loc='left', fontsize=9)
        plt.legend()
        plt.show()


    @staticmethod
    def control_limts_definition(analysis_data, mean):

        xi, xi_1 = tee(analysis_data)
        next(xi_1, None)
        at = [abs(b - a) for a, b in zip(xi, xi_1)]
        atmn = np.mean(at)

        lcs = mean + 2.66 * atmn
        lci = mean - 2.66 * atmn

        if lci <= 0:
            lci = 0

        return [lcs, lci]