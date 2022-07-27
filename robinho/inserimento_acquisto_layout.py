from PySide6.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout, QLabel
from robinho.single_field import SingleField


class InserimentoAcquistoLayout(QVBoxLayout):
    def __init__(self) -> None:
        super().__init__()

        self._button_slot_model = None
        title = QLabel()
        title.setText("Assegna un giocatore:")
        self.addWidget(title)

        fields_layout = QHBoxLayout()
        self._nome = SingleField("Nome")
        self._squadra = SingleField("Squadra")
        self._prezzo = SingleField("Prezzo")
        self._confirm_button = QPushButton("Inserisci")
        self._confirm_button.clicked.connect(self._button_slot)

        fields_layout.addWidget(self._nome)
        fields_layout.addWidget(self._squadra)
        fields_layout.addWidget(self._prezzo)
        fields_layout.addWidget(self._confirm_button)

        self.addLayout(fields_layout)

    def _button_slot(self) -> None:
        nome = self._nome.text()
        prezzo = int(self._prezzo.text())
        squadra = self.squadra.text()

        self._button_slot_model(nome, squadra, prezzo)

    def set_button_slot(self, slot) -> None:
        self._button_slot_model = slot
