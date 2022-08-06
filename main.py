import fire
from PySide6.QtWidgets import QApplication
import sys

from robinho.asta_model import AstaModel
from robinho.const import DEFAULT_CREDITI
from robinho.layouts.main_window import MainWindow

NOME_LEGA = "Maronne League"
NOMI_SQUADRE = [
    "Injured FC",
    "I fuffoli",
    "Parmareggio",
    "GrifonDoro",
    "RealMalvasia79",
    "FC Gigio",
    "Fossa dei leoni",
    "ScaccoFC",
]


def main(nome_lega: str = NOME_LEGA, crediti_iniziali: int = DEFAULT_CREDITI):
    asta_model = AstaModel(
        nome_lega=nome_lega,
        crediti_iniziali=crediti_iniziali,
        nomi_squadre=NOMI_SQUADRE,
    )

    app = QApplication(sys.argv)
    main_window = MainWindow(asta_model)
    # main_window.setStyleSheet(
    #     "color: white; background-color: #020441; selection-color: #faa001"
    # )
    main_window.showMaximized()

    app.exec()


if __name__ == "__main__":
    fire.Fire(main)
