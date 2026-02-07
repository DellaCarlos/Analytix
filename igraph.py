from abc import ABC, abstractmethod

from pandas import DataFrame


class IGraph(ABC):

    @staticmethod
    @abstractmethod
    def show(df: DataFrame, **kwargs):
        ...

