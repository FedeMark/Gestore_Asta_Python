from typing import List
import pandas as pd
from robinho.Lega import Lega
from robinho.pandas_model import PandasModel


class AstaModel:
    def __init__(self, lega: Lega) -> None:
        self._lega = lega

    def get_listone_model(self, ruoli: List[str]):
        return PandasModel(self._lega.get_listone(ruoli=ruoli))

    def get_nome_lega(self) -> str:
        return self._lega.get_nome()

    def get_stats_model(self):
        return PandasModel(self._lega.get_stats_squadre())

    def get_rosa_model(self, index: int = 0):
        return PandasModel(self._lega.get_squadra_rosa(index))

    def get_nomi_giocatori(self) -> List[str]:
        return self._lega.get_nomi_giocatori()

    def get_nomi_squadre(self) -> List[str]:
        return self._lega.get_nomi_squadre()

    def inserisci_giocatore(
        self,
        nome_squadra: str,
        nome: str,
        prezzo: int,
    ) -> bool:
        result = self._lega.inserisci_giocatore(
            nome_squadra=nome_squadra, nome=nome, prezzo=prezzo
        )

        self.save_data()

        return result

    def load_data(self) -> None:
        self._lega = Lega.load_data(nome_lega=self._lega._nome_lega)

    def save_data(self):
        self._lega.save_data()
