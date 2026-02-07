import pandas as pd
from data import Data
from filtros import *
from ifiltro import IFiltro
from typing import Type
from metodos import *
import openpyxl


class LeituraCsv:

    def __init__(self, path: str):
        self.df = pd.read_csv(path, sep=';', header=0, encoding='unicode_escape')

    def filtrar(self, filtro: Type[IFiltro] = None, **kwargs):
        if filtro:
            return Data(filtro.filtro(self.df, **kwargs), **kwargs)
        return Data(self.df, **kwargs)


if __name__ == "__main__":
    _path = 'path.csv'
    csv = LeituraCsv(path=_path)

    filtros = {
        'loc': Loc,
        'produto': Produto,
        'loc_produto': LocProduto
    }

    col = _path.split('/')[-1].split('.')[0]
    hist = csv.filtrar(
        filtro=filtros.get("produto"),
        loc="-",
        produto=10317,
        ref=45,
        coluna=col
    )

    hist.show(Information)
    hist.show(Distribuicao)
    hist.show(CartaControleAmplitude)
