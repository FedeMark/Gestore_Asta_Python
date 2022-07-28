from __future__ import annotations
import os
from pathlib import Path
from typing import List
import numpy as np
import pandas as pd

from robinho.Squadra import Squadra

from robinho.const import (
    DEFAULT_CREDITI,
    DEFAULT_SAVE_PATH,
    LISTONE_COLUMNS,
    LISTONE_PATH,
)


class Lega:
    def __init__(
        self,
        nome_lega: str,
        nomi_squadre: List[str],
        path_listone: Path = LISTONE_PATH,
        crediti_iniziali: int = DEFAULT_CREDITI,
    ) -> None:
        self._crediti_iniziali = crediti_iniziali
        self._listone = pd.read_csv(path_listone, index_col=0)
        self._listone[LISTONE_COLUMNS[3]] = self._listone[LISTONE_COLUMNS[3]].astype(
            "int"
        )
        self._nome_lega = nome_lega

        if nomi_squadre is not None:
            self._squadre = {
                nome: Squadra(crediti_iniziali=crediti_iniziali, nome_squadra=nome)
                for nome in nomi_squadre
            }

    def save_data(self, save_path: Path = DEFAULT_SAVE_PATH) -> None:
        dir_path = save_path / self._nome_lega

        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        self._listone.to_csv(dir_path / "listone.csv")

        np.savez(
            dir_path / (self._nome_lega + ".npz"),
            nome_lega=self._nome_lega,
            nomi_squadre=list(self._squadre.keys()),
            crediti_iniziali=self._crediti_iniziali,
        )

        squadre_dir_path = dir_path / "Squadre"

        if not os.path.exists(squadre_dir_path):
            os.mkdir(squadre_dir_path)
        for squadra in self._squadre.values():
            squadra.save_data(squadre_dir_path)

    def get_listone(self) -> pd.DataFrame:
        return self._listone

    def get_nome(self) -> str:
        return self._nome_lega

    def get_nomi_giocatori(self) -> List[str]:
        return self._listone[LISTONE_COLUMNS[1]].values

    def get_nomi_squadre(self) -> List[str]:
        return list(self._squadre.keys())

    def get_stats_squadre(self) -> pd.DataFrame():
        stats = pd.concat([squadra.get_stats() for squadra in self._squadre.values()])
        stats.reset_index(inplace=True)
        stats.drop(columns=["index"], inplace=True)
        stats.sort_values(by="IQR", ascending=False, inplace=True)

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

    def save_data(self, save_path: Path = DEFAULT_SAVE_PATH) -> None:
        dir_path = save_path / self._nome_lega

        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        self._listone.to_csv(dir_path / "listone.csv")

        np.savez(
            dir_path / (self._nome_lega + ".npz"),
            nome_lega=self._nome_lega,
            nomi_squadre=list(self._squadre.keys()),
            crediti_iniziali=self._crediti_iniziali,
        )

        squadre_dir_path = dir_path / "Squadre"

        if not os.path.exists(squadre_dir_path):
            os.mkdir(squadre_dir_path)
        for squadra in self._squadre.values():
            squadra.save_data(squadre_dir_path)

    @classmethod
    def load_data(
        cls, load_path: Path = DEFAULT_SAVE_PATH, nome_lega: str = "Fantalega"
    ) -> Lega:
        dir_path = load_path / nome_lega

        info_lega = np.load(dir_path / (nome_lega + ".npz"))
        nome_lega = info_lega["nome_lega"]
        nomi_squadre = info_lega["nomi_squadre"]
        crediti_iniziali = info_lega["crediti_iniziali"]

        lega = cls(
            nome_lega=nome_lega,
            path_listone=dir_path / "listone.csv",
            crediti_iniziali=crediti_iniziali,
            nomi_squadre=nomi_squadre,
        )

        for squadra in lega._squadre.values():
            squadra.load_data(dir_path / "Squadre")

        return lega
