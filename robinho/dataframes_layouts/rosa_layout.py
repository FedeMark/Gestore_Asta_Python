from typing import List
from PySide6.QtWidgets import QVBoxLayout, QTableView, QComboBox


class RosaLayout(QVBoxLayout):
    def __init__(self, squadre: List[str]):
        super().__init__()

        self._rosa_widget = QTableView()
        self.addWidget(self._rosa_widget)

        self._squadra_choice = QComboBox()
        self._squadra_choice.addItems(squadre)
        self.addWidget(self._squadra_choice)

    def set_model(self, model):
        self._rosa_widget.setModel(model)

    def set_combobox_slot(self, slot):
        self._squadra_choice.currentIndexChanged.connect(slot)

    def get_combobox_index(self) -> int:
        return self._squadra_choice.currentIndex()
