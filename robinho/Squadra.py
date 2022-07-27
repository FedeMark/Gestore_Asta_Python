import pandas as pd
from robinho.Rosa import COLUMNS, Rosa
from robinho.const import DEFAULT_CREDITI

STATS_COLUMNS = ["Squadra", "Crediti_rimasti", "Valore", "IQR"]


class Squadra:
    def __init__(
        self, nome_squadra: str, crediti_iniziali: int = DEFAULT_CREDITI
    ) -> None:
        self._crediti_iniziali = crediti_iniziali
        self._credit = crediti_iniziali
        self._nome = nome_squadra
        self._rosa = Rosa()

    def get_stats(self) -> pd.DataFrame:
        valore_totale = self._rosa.get_valore()
        spesa_totale = self._rosa.get_spesa()
        if spesa_totale == 0:
            spesa_totale_div = 1
        else:
            spesa_totale_div = spesa_totale

        data_dict = dict(
            zip(
                STATS_COLUMNS,
                [
                    self._nome,
                    self._crediti_iniziali - spesa_totale,
                    valore_totale,
                    valore_totale / spesa_totale_div,
                ],
            )
        )

        return pd.DataFrame(data_dict, index=[0])

    def get_rosa(self) -> pd.DataFrame:
        return self._rosa.get_data()

    def inserisci_giocatore(self, ruolo: str,  nome: str, prezzo: int, valore: int):
      self._rosa.inserisci_giocatore(ruolo,nome,prezzo, valore)