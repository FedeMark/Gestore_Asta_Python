from typing import List
from PySide6.QtWidgets import QHBoxLayout, QCheckBox


class RuoliCheckboxes(QHBoxLayout):
    def __init__(self, labels: List[str] = None) -> None:
        super().__init__()
        self._checkboxes = []

        for label in labels:
            checkbox = QCheckBox(label)  # .setChecked(True)
            checkbox.setChecked(True)
            self.addWidget(checkbox)
            self._checkboxes.append(checkbox)

    def get_checked(self) -> List[str]:
        return [
            checkbox.text() for checkbox in self._checkboxes if checkbox.isChecked()
        ]

    def set_slot(self, slot):
        for checkbox in self._checkboxes:
            checkbox.stateChanged.connect(slot)
