import sys
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QApplication)

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.line1 = QLineEdit()
        self.line1.setValidator(QIntValidator())
        self.line2 = QLineEdit()
        self.line2.setValidator(QIntValidator())
        self.btn1 = QPushButton('Test', self)

        self.line1.textChanged.connect(self.calculated)


        vbox = QVBoxLayout()
        vbox.addWidget(self.line1)
        #vbox.addWidget(self.line3)
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.line2)

        self.setLayout(vbox)

        self.setGeometry(600, 400, 400, 400)
        self.setWindowTitle('Test')

    def calculated(self, text):
        if text:
            text = (int(text) * 2)
            self.line2.setText(str(text))
        else: self.line2.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

