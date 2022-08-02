from typing import List
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QTableView,
    QMessageBox,
    QMainWindow,
)

from PySide6.QtGui import QAction
from robinho.asta_model import AstaModel
from robinho.dataframes_layouts.rosa_layout import RosaLayout

from robinho.inserimento_acquisto_layout import InserimentoAcquistoLayout
from robinho.ruoli_checkboxes import RuoliCheckboxes


class MainWindow(QMainWindow):
    def __init__(self, model: AstaModel) -> None:
        super().__init__()

        self._asta_model = model

        self._init_ui()

    def _change_rosa_view(self, index):
        self._set_rosa_model(index)

    def _create_menu(self):
        menubar = self.menuBar()

        save_action = QAction("&Save", self)
        save_action.triggered.connect(self._save_data)
        menubar.addAction(save_action)

        load_action = QAction("&Load", self)
        load_action.triggered.connect(self._load_data)
        menubar.addAction(load_action)

    def _get_dataframes_layout(self):
        dataframes_layout = QHBoxLayout()

        left_layout = QVBoxLayout()
        self._listone_widget = QTableView()
        self._listone_checkboxes = RuoliCheckboxes(["P", "D", "C", "A"])
        left_layout.addLayout(self._listone_checkboxes)
        left_layout.addWidget(self._listone_widget)

        self._rosa_layout = RosaLayout(self._asta_model.get_nomi_squadre())
        self._rosa_layout.set_combobox_slot(self._change_rosa_view)

        right_layout = QVBoxLayout()
        self._stats_widget = QTableView()
        right_layout.addWidget(self._stats_widget)

        dataframes_layout.addLayout(left_layout)
        dataframes_layout.addLayout(self._rosa_layout)
        dataframes_layout.addLayout(right_layout)

        return dataframes_layout

    def _init_ui(self):

        self.setWindowTitle("Asta della lega: " + self._asta_model.get_nome_lega())
        self._create_menu()

        main_layout = QVBoxLayout()

        self._inserimento_acquisto_layout = InserimentoAcquistoLayout(
            squadre=self._asta_model.get_nomi_squadre(),
            nomi_giocatori=self._asta_model.get_nomi_giocatori(),
        )
        self._inserimento_acquisto_layout.set_button_slot(self._inserisci_giocatore)
        main_layout.addLayout(self._inserimento_acquisto_layout)

        dataframes_layout = self._get_dataframes_layout()

        main_layout.addLayout(dataframes_layout)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self._set_listone_model()
        self._set_rosa_model()
        self._set_stats_model()

        self._listone_checkboxes.set_slot(self._checkboxes_slot)

    def _checkboxes_slot(self):
        ruoli = self._listone_checkboxes.get_checked()
        self._set_listone_model(ruoli=ruoli)

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
            self._update_views()
            self._save_data()
            self._inserimento_acquisto_layout.reset()
            self._inserimento_acquisto_layout.update_nomi(
                self._asta_model.get_nomi_giocatori()
            )
        else:
            dialog = QMessageBox(self)
            dialog.setText("Giocatore non presente in lista o già assegnato.")
            dialog.exec()

    def _load_data(self) -> None:
        self._asta_model.load_data()

        self._update_views()

    def _save_data(self) -> None:
        self._asta_model.save_data()

    def _set_listone_model(self, ruoli: List[str] = ["P", "D", "C", "A"]) -> None:
        listone_model = self._asta_model.get_listone_model(ruoli=ruoli)
        self._listone_widget.setModel(listone_model)

    def _set_rosa_model(self, index: int = 0) -> None:
        rosa_model = self._asta_model.get_rosa_model(index)
        self._rosa_layout.set_model(rosa_model)

    def _set_stats_model(self) -> None:
        stats_model = self._asta_model.get_stats_model()
        self._stats_widget.setModel(stats_model)

    def _show_squadra(self, item) -> None:
        print(item)

    def _update_views(self) -> None:
        self._set_listone_model()
        self._set_rosa_model(self._rosa_layout.get_combobox_index())
        self._set_stats_model()
