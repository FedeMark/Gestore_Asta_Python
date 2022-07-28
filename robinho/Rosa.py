import pandas as pd

from robinho.const import ROSA_DF_COLUMNS

COLUMNS = ["Ruolo", "Giocatore", "Prezzo", "Valore"]


class Rosa:
    def __init__(self) -> None:
        self._acquisti = pd.DataFrame(columns=ROSA_DF_COLUMNS)
        self._data = pd.DataFrame(columns=COLUMNS)

    def inserisci_giocatore(self, ruolo: str, nome: str, prezzo: int, valore: int):
        nuovo_giocatore_dict = dict(zip(COLUMNS, [ruolo, nome, prezzo, valore]))
        nuovo_giocatore = pd.DataFrame(nuovo_giocatore_dict, index=[0])
        self._data = pd.concat([self._data, nuovo_giocatore])

    def get_spesa(self) -> int:
        return self._data[COLUMNS[2]].sum()

    def get_valore(self) -> int:
        return self._data[COLUMNS[3]].sum()

    def get_data(self) -> pd.DataFrame:
        return self._data
