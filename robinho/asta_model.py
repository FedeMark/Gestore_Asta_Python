import pandas as pd
from robinho.Lega import Lega
from robinho.pandas_model import PandasModel


class AstaModel:
    def __init__(self, lega: Lega) -> None:
        self._lega = lega

    def get_listone_model(self):
        return PandasModel(self._lega.get_listone())

    def get_stats_model(self):
        return PandasModel(self._lega.get_stats_squadre())

    def get_rosa_model(self, index: int = 0):
        return PandasModel(self._lega.get_squadra_rosa(index))
