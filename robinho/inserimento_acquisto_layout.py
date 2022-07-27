from PySide6.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout
from robinho.single_field import SingleField

class InserimentoAcquistoLayout(QVBoxLayout):
  def __init__(self, text: str) -> None:
        super().__init__()
        
        title = QLabel()
        title.setText("Assegna un giocatore:")
        self.addWidget(title)
        
        fields_layout = QHBoxLayout()
        self._nome = SingleField()
        self._squadra = SingleField()
        self._prezzo = SingleField()
        self._confirm_button = QPushButton("Inserisci")
        
        fields_layout.addWidget(self._nome)
        fields_layout.addWidget(self._squadra)
        fields_layout.addWidget(self._prezzo)
        fields_layout.addWidget(self._confirm_button)
        
        self.addLayout(fields_layout)
        
        
  def set_button_listener(self, listener) -> :
    self._confirm_button.clicked.connect(listener)
    