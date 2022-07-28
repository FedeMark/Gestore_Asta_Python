from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QTableView, QMessageBox
from robinho.asta_model import AstaModel

from robinho.inserimento_acquisto_layout import InserimentoAcquistoLayout


class MainWindow(QWidget):
    def __init__(self, model: AstaModel) -> None:
        super().__init__()

        self._asta_model = model

        self._init_ui()

    def _init_ui(self):
        main_layout = QVBoxLayout()

        self._inserimento_acquisto_layout = InserimentoAcquistoLayout(
            squadre=self._asta_model.get_nomi_squadre(),
            nomi_giocatori=self._asta_model.get_nomi_giocatori(),
        )
        self._inserimento_acquisto_layout.set_button_slot(self._inserisci_giocatore)
        main_layout.addLayout(self._inserimento_acquisto_layout)

        dataframes_layout = QHBoxLayout()

        left_layout = QVBoxLayout()
        self._listone_widget = QTableView()
        left_layout.addWidget(self._listone_widget)

        center_layout = QVBoxLayout()
        self._rosa_widget = QTableView()
        center_layout.addWidget(self._rosa_widget)

        right_layout = QVBoxLayout()
        self._stats_widget = QTableView()
        right_layout.addWidget(self._stats_widget)

        dataframes_layout.addLayout(left_layout)
        dataframes_layout.addLayout(center_layout)
        dataframes_layout.addLayout(right_layout)

        main_layout.addLayout(dataframes_layout)

        self.setLayout(main_layout)

        self._set_listone_model()
        self._set_rosa_model()
        self._set_stats_model()

    def _set_listone_model(self) -> None:
        listone_model = self._asta_model.get_listone_model()
        self._listone_widget.setModel(listone_model)

    def _set_rosa_model(self) -> None:
        rosa_model = self._asta_model.get_rosa_model()
        self._rosa_widget.setModel(rosa_model)

    def _set_stats_model(self) -> None:
        stats_model = self._asta_model.get_stats_model()
        self._stats_widget.setModel(stats_model)

    def _inserisci_giocatore(
        self,
        nome_squadra: str,
        nome: str,
        prezzo: int,
    ) -> None:
        result = self._asta_model.inserisci_giocatore(
            nome_squadra=nome_squadra, nome=nome, prezzo=prezzo
        )

        if result:
            self._set_listone_model()
            self._set_rosa_model()
            self._set_stats_model()
        else:
            dialog = QMessageBox(self)
            dialog.setText("Giocatore non presente in lista o già assegnato.")
            dialog.exec()
