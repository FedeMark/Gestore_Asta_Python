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

    app = QApplication(sys.argv)
    main_window = MainWindow(asta_model)
    main_window.show()

    app.exec()


if __name__ == "__main__":
    fire.Fire(main)
