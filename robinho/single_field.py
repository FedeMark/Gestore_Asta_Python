from typing import List
from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QComboBox, QCompleter


class SingleField(QHBoxLayout):
    def __init__(
        self, text: str, choices: List[str] = None, completer_list: List[str] = None
    ) -> None:
        super().__init__()

        self._label = QLabel()
        self._label.setText(text)
        self._choices = choices

        if choices is None:
            self._field = QLineEdit()

            if completer_list is not None:
                completer = QCompleter(completer_list)
                self._field.setCompleter(completer)

        else:
            self._field = QComboBox()
            self._field.addItems(choices)

        self.addWidget(self._label)
        self.addWidget(self._field)

    def get_input(self) -> str:
        if self._choices is None:
            return self._field.text()

        return self._field.currentText()

    def reset(self) -> None:
        if self._choices is None:
            self._field.setText('')