from typing import List
from PySide6.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout, QLabel
from robinho.single_field import SingleField


class InserimentoAcquistoLayout(QVBoxLayout):
    def __init__(self, squadre: List[str], nomi_giocatori: List[str]) -> None:
        super().__init__()

        self._button_slot_model = None
        title = QLabel()
        title.setText("Assegna un giocatore:")
        self.addWidget(title)

        fields_layout = QHBoxLayout()
        self._nome = SingleField("Nome", completer_list=nomi_giocatori)
        self._squadra = SingleField("Squadra", choices=squadre)
        self._prezzo = SingleField("Prezzo")
        self._confirm_button = QPushButton("Inserisci")
        self._confirm_button.clicked.connect(self._button_slot)

        fields_layout.addLayout(self._nome)
        fields_layout.addLayout(self._squadra)
        fields_layout.addLayout(self._prezzo)
        fields_layout.addWidget(self._confirm_button)

        self.addLayout(fields_layout)

    def _button_slot(self) -> None:
        nome = self._nome.get_input()
        prezzo = int(self._prezzo.get_input())
        squadra = self._squadra.get_input()

        self._button_slot_model(nome_squadra=squadra, nome=nome, prezzo=prezzo)

    def set_button_slot(self, slot) -> None:
        self._button_slot_model = slot
