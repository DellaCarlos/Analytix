from data import Data
from ifiltro import IFiltro
from pandas import DataFrame


class Loc(IFiltro):
    """
    Filtra apenas 'loc'.
    """

    @staticmethod
    def filtro(df: DataFrame, **kwargs) -> DataFrame:
        _df = df.query('loc == {}'.format(kwargs.get('loc')))
        return _df

