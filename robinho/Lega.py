from pathlib import Path
from typing import List

import pandas as pd
from robinho.Squadra import Squadra

from robinho.const import DEFAULT_CREDITI, LISTONE_COLUMNS, LISTONE_PATH


class Lega:
    def __init__(
        self,
        nome_lega: str,
        nomi_squadre: List[str],
        path_listone: Path = LISTONE_PATH,
        crediti_iniziali: int = DEFAULT_CREDITI,
    ) -> None:
        self._listone = pd.read_csv(path_listone, index_col=0)
        self._listone[LISTONE_COLUMNS[3]] = self._listone[LISTONE_COLUMNS[3]].astype(
            "int"
        )
        self._nome_lega = nome_lega
        self._squadre = {
            nome: Squadra(crediti_iniziali=crediti_iniziali, nome_squadra=nome)
            for nome in nomi_squadre
        }

    def load(self) -> None:
        pass

    def save(self) -> None:
        pass

    def get_listone(self) -> pd.DataFrame:
        return self._listone

    def get_nomi_giocatori(self) -> List[str]:
        return self._listone[LISTONE_COLUMNS[1]].values

    def get_nomi_squadre(self) -> List[str]:
        return list(self._squadre.keys())

    def get_stats_squadre(self) -> pd.DataFrame():
        stats = pd.concat([squadra.get_stats() for squadra in self._squadre.values()])
        stats.reset_index(inplace=True)

        return stats

    def get_squadra_rosa(self, index: int = 0) -> pd.DataFrame:
        return list(self._squadre.values())[index].get_rosa()

    def inserisci_giocatore(
        self,
        nome_squadra: str,
        nome: str,
        prezzo: int,
    ) -> bool:
        listone = self._listone

        giocatore = listone[listone[LISTONE_COLUMNS[1]] == nome]

        if giocatore.shape[0] == 0:
            return False

        assert giocatore.shape[0] == 1

        giocatore = giocatore.iloc[0]
        ruolo = giocatore[LISTONE_COLUMNS[0]]
        valore = giocatore[LISTONE_COLUMNS[3]]

        self._squadre[nome_squadra].inserisci_giocatore(ruolo, nome, prezzo, valore)
        self._listone = listone[listone[LISTONE_COLUMNS[1]] != nome]

        return True
