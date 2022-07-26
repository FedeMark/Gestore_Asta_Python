from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QTableView,
    QLineEdit,
    QLabel,
)
import pandas as pd
from robinho.Squadra import Squadra

from robinho.pandas_model import PandasModel


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self._init_ui()

    def _init_ui(self):
        main_layout = QHBoxLayout()

        left_layout = QVBoxLayout()

        nuovo_acquisto_layout = QVBoxLayout()
        title = QLabel()
        title.setText("Assegna un giocatore:")
        nuovo_acquisto_layout.addWidget(title)
        inserimento_acquisto_layout = QHBoxLayout()

        nuovo_acquisto_layout.addLayout(inserimento_acquisto_layout)
        left_layout.addLayout(nuovo_acquisto_layout)

        self._listone_widget = QTableView()
        left_layout.addWidget(self._listone_widget)

        center_layout = QVBoxLayout()
        self._rosa_widget = QTableView()
        center_layout.addWidget(self._rosa_widget)

        right_layout = QVBoxLayout()
        self._stats_widget = QTableView()
        right_layout.addWidget(self._stats_widget)

        main_layout.addLayout(left_layout)
        main_layout.addLayout(center_layout)
        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)
        self.show()

    def set_listone_model(self, listone_model) -> None:
        self._listone_widget.setModel(listone_model)

    def set_rosa_model(self, rosa_model) -> None:
        self._rosa_widget.setModel(rosa_model)

    def set_stats_model(self, stats_model) -> None:
        self._stats_widget.setModel(stats_model)
