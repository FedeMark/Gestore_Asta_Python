from typing import List
import fire
from PySide6.QtWidgets import QApplication
import sys

from robinho.Lega import Lega
from robinho.asta_model import AstaModel
from robinho.main_window import MainWindow


def main():  # nome_lega: str, nomi_squadre: List[str]):
    lega = Lega(nome_lega="Fantalega", nomi_squadre=["S1", "S2"])
    asta_model = AstaModel(lega)

    app = QApplication([])

    main_window = MainWindow()
    main_window.set_listone_model(asta_model.get_listone_model())
    main_window.set_rosa_model(asta_model.get_rosa_model())
    main_window.set_stats_model(asta_model.get_stats_model())
    main_window.set_inserimento_acquisto_button_slot(asta_model.inserisci_giocatore)