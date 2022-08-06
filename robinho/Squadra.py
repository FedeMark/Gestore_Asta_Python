from __future__ import annotations
from pathlib import Path
import numpy as np
import pandas as pd
from robinho.Rosa import Rosa
from robinho.const import DEFAULT_CREDITI, ROSA_DF_COLUMNS
from robinho.utils import get_series_value

STATS_COLUMNS = ["Squadra", "Crediti_rimasti", "Valore", "IQR", "P", "D", "C", "A"]


class Squadra:
    def __init__(
        self, nome_squadra: str, crediti_iniziali: int = DEFAULT_CREDITI
    ) -> None:
        self._crediti_iniziali = crediti_iniziali
        self._nome = nome_squadra
        self._rosa = Rosa()

    def get_stats(self) -> pd.DataFrame:
        valore_totale = self._rosa.get_valore()
        spesa_totale = self._rosa.get_spesa()
        if spesa_totale == 0:
            spesa_totale_div = 1
        else:
            spesa_totale_div = spesa_totale

        counts = self._rosa.get_data()[ROSA_DF_COLUMNS[0]].value_counts()

        data_dict = dict(
            zip(
                STATS_COLUMNS,
                [
                    self._nome,
                    self._crediti_iniziali - spesa_totale,
                    valore_totale,
                    round(valore_totale / spesa_totale_div, 2),
                    get_series_value(counts, "P"),
                    get_series_value(counts, "D"),
                    get_series_value(counts, "C"),
                    get_series_value(counts, "A"),
                ],
            )
        )

        return pd.DataFrame(data_dict, index=[0])

    def get_rosa(self) -> pd.DataFrame:
        return self._rosa.get_data()

    def inserisci_giocatore(
        self, ruolo: str, nome: str, prezzo: int, valore: int, slot: int
    ):
        self._rosa.inserisci_giocatore(ruolo, nome, prezzo, valore, slot)

    def save_data(self, save_path: Path):
        data = self._rosa.get_data_to_save()
        data.to_csv(save_path / (self._nome + ".csv"))

    def load_data(self, load_path: Path) -> None:
        data = pd.read_csv(load_path / (self._nome + ".csv"), index_col=0)
        self._rosa.set_data(data)
