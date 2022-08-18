from typing import List
from unittest.mock import patch
import pandas as pd
from robinho.Lega import Lega
from robinho.const import LISTONE_CLASSIC_PATH, LISTONE_MANTRA_PATH
from robinho.pandas_model import PandasModel


class AstaModel:
    def __init__(
        self,
        nome_lega: str,
        crediti_iniziali: int,
        nomi_squadre: List[str],
        mantra: bool,
    ) -> None:
        self._nome_lega = nome_lega
        loaded = self.load_data()
        self._mantra = mantra

        if not loaded:
            self._lega = Lega(
                nome_lega=nome_lega,
                crediti_iniziali=crediti_iniziali,
                nomi_squadre=nomi_squadre,
            )

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

    @property
    def mantra(self):
        return self._mantra

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

    def load_data(self) -> bool:
        result = Lega.load_data(nome_lega=self._nome_lega)
        success = result[0]

        if success:
            self._lega = result[1]

        return success

    def save_data(self):
        self._lega.save_data()
