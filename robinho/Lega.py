from pathlib import Path
from typing import List

import pandas as pd
from robinho.Squadra import Squadra

from robinho.const import DEFAULT_CREDITI, LISTONE_PATH


class Lega:
    def __init__(
        self,
        nome_lega: str,
        nomi_squadre: List[str],
        path_listone: Path = LISTONE_PATH,
        crediti_iniziali: int = DEFAULT_CREDITI,
    ) -> None:
        self._listone = pd.read_csv(path_listone, index_col=0)
        self._nome_lega = nome_lega
        self._squadre = [
            Squadra(crediti_iniziali=crediti_iniziali, nome_squadra=nome)
            for nome in nomi_squadre
        ]

    def load(self) -> None:
        pass

    def save(self) -> None:
        pass

    def get_listone(self) -> pd.DataFrame:
        return self._listone

    def get_stats_squadre(self) -> pd.DataFrame():
        stats = pd.concat([squadra.get_stats() for squadra in self._squadre])
        stats.reset_index(inplace=True)

        return stats

    def get_squadra_rosa(self, index: int = 0) -> pd.DataFrame:
        return self._squadre[index].get_rosa()
