from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit

class SingleField(QHBoxLayout):
  def __init__(self, text: str) -> None:
        super().__init__()
        
        self._label = QLabel()
        self._label.setText(text)
        self._field = QLineEdit()
        
        self.addWidget(self._label)
        self.addWidget(self._field)
        
  def get_input(self) -> :
    return self._field.text()
    