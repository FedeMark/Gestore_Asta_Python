import pandas as pd

from robinho.const import ROSA_DF_COLUMNS


class Rosa:
    def __init__(self) -> None:
        self._data = pd.DataFrame(columns=ROSA_DF_COLUMNS)

    def inserisci_giocatore(
        self, ruolo: str, nome: str, prezzo: int, valore: int, slot: int
    ):
        nuovo_giocatore_dict = dict(
            zip(ROSA_DF_COLUMNS, [ruolo, nome, prezzo, valore, slot])
        )
        nuovo_giocatore = pd.DataFrame(nuovo_giocatore_dict, index=[0])
        self._data = pd.concat([self._data, nuovo_giocatore])

    def get_spesa(self) -> int:
        return self._data[ROSA_DF_COLUMNS[2]].sum()

    def get_valore(self) -> int:
        return self._data[ROSA_DF_COLUMNS[3]].sum()

    def get_data(self) -> pd.DataFrame:
        data = self._data.sort_values(
            by=[ROSA_DF_COLUMNS[0], ROSA_DF_COLUMNS[4]], ascending=[False, False]
        )
        return data[[ROSA_DF_COLUMNS[0], ROSA_DF_COLUMNS[1], ROSA_DF_COLUMNS[4]]]

    def get_data_to_save(self) -> pd.DataFrame:
        return self._data

    def set_data(self, data: pd.DataFrame) -> None:
        self._data = data
