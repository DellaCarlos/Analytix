from typing import Type
from pandas import DataFrame
from igraph import IGraph


class Data:
    def __init__(self, df: DataFrame, **kwargs):
        self.df = df
        self.param = kwargs

    def show(self, metodo: Type[IGraph]):
        metodo.show(self.df, **self.param)
