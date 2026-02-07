from ifiltro import IFiltro
from pandas import DataFrame

class LocProduto(IFiltro):
    """
    Filtra simultaneamente 'loc' e 'produto'.
    """

    @staticmethod
    def filtro(df: DataFrame, **kwargs) -> DataFrame:
        _df = df.query('loc == {}'.format(kwargs.get('loc')))
        _df = _df.query('produto == {}'.format(kwargs.get('produto')))
        return _df
