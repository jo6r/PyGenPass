import string
import sys
import random
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QComboBox, QApplication, QPushButton, QLineEdit, \
    QVBoxLayout, QCheckBox

PWD_LENGTH_MIN = 6
PWD_LENGTH_MAX = 21


class PassGenerator:

    def __init__(self):
        self._special_chars = "*#@"
        self._character_set = ""

    @property
    def special_char(self):
        return self._special_chars

    @property
    def character_set(self):
        return self._character_set

    def enable_alfa(self):
        self._character_set += string.ascii_letters

    def enable_digits(self):
        self._character_set += string.digits

    def enable_special(self):
        self._character_set += self._special_chars

    def gen_pwd(self, length) -> str:
        return ''.join(random.choice(self._character_set) for i in range(length))


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("PyGenPass")
        icon = QIcon("key.png")
        self.setWindowIcon(icon)

        layout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(QLabel("Length"), 0, 0)

        self.combo = QComboBox()
        self.combo.setFixedWidth(100)
        pod_length_list = list()
        for n in range(PWD_LENGTH_MIN, PWD_LENGTH_MAX):
            pod_length_list.append(str(n))
        self.combo.addItems(pod_length_list)
        layout.addWidget(self.combo, 0, 1)

        vbox = QVBoxLayout()
        layout.addLayout(vbox, 0, 2)

        self.checkbox_alfa = QCheckBox("alfa")
        self.checkbox_alfa.setChecked(True)
        self.checkbox_digits = QCheckBox("digits")
        self.checkbox_digits.setChecked(True)
        self.checkbox_special = QCheckBox(PassGenerator().special_char)
        self.checkbox_special.setChecked(True)
        vbox.addWidget(self.checkbox_alfa)
        vbox.addWidget(self.checkbox_digits)
        vbox.addWidget(self.checkbox_special)

        button = QPushButton("Generate")
        button.clicked.connect(self.button_clicked_handler)
        layout.addWidget(button, 1, 0)

        self.output_line = QLineEdit()
        layout.addWidget(self.output_line, 1, 1)

    def button_clicked_handler(self):
        pg = PassGenerator()
        if self.checkbox_alfa.isChecked():
            pg.enable_alfa()
        if self.checkbox_digits.isChecked():
            pg.enable_digits()
        if self.checkbox_special.isChecked():
            pg.enable_special()

        if pg.character_set:
            text = pg.gen_pwd(int(self.combo.currentText()))
        else:
            text = "select character set"

        self.output_line.setText(text)


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.resize(400, 200)
    widget.show()
    sys.exit(app.exec())
