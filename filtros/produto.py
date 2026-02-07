from ifiltro import IFiltro
from pandas import DataFrame


class Produto(IFiltro):
    """
    Filtra apenas 'produto'.
    """

    @staticmethod
    def filtro(df: DataFrame, **kwargs) -> DataFrame:
        _df = df.query('produto == {}'.format(kwargs.get('produto')))
        return _df
