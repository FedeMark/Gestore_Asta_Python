import fire
from PySide6.QtWidgets import QApplication
import sys

from robinho.asta_model import AstaModel
from robinho.const import DEFAULT_CREDITI
from robinho.layouts.main_window import MainWindow

NOME_LEGA = "Mantra_Diemmi"
NOMI_SQUADRE = [
    "Injured FC",
    "I gufi",
    "AC Picchia",
    "Pennic Hellas",
    "banane",
    "Mapi FC",
    "Atletico Bino",
    "Team A",
]


def main(
    nome_lega: str = NOME_LEGA,
    crediti_iniziali: int = 500,
    mantra: bool = True,
):
    asta_model = AstaModel(
        nome_lega=nome_lega,
        crediti_iniziali=crediti_iniziali,
        nomi_squadre=NOMI_SQUADRE,
        mantra=mantra,
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
