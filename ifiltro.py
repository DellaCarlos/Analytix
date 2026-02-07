from abc import ABC, abstractmethod
from pandas import DataFrame


class IFiltro(ABC):

    @staticmethod
    @abstractmethod
    def filtro(df: DataFrame, **kwargs) -> DataFrame:
        ...

