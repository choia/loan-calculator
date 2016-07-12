import sys
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLineEdit, QLabel


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Test")
        self.qline1 = QLineEdit()
        self.qline1.setValidator(QDoubleValidator(0.0, 999999.99, 2))
        self.qline2 = QLineEdit()
        self.qline2.setValidator(QDoubleValidator(0.0, 999999.99, 2))
        self.qline3 = QLineEdit()
        self.qline3.setValidator(QIntValidator())
        self.qline4 = QLineEdit()
        self.qline4.setValidator(QIntValidator())

        self.qline1.setPlaceholderText("Enter your number!")
        self.qlabel1 = QLabel(self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.qline1)
        vbox.addWidget(self.qline2)
        vbox.addWidget(self.qline3)
        vbox.addWidget(self.qline4)
        vbox.addWidget(self.qlabel1)
        vbox.addStretch(1)
        self.setLayout(vbox)

        self.qline1.textEdited.connect(self.text_updated)
        self.qline2.textEdited.connect(self.text_updated)
        self.qline3.textEdited.connect(self.text_updated)
        self.qline4.textEdited.connect(self.text_updated)

    def text_updated(self):
        if self.qline1.text() and self.qline2.text() and self.qline3.text() and self.qline4.text():
            print('yes')
            q1 = float(self.qline1.text())
            q2 = float(self.qline2.text())
            q3 = int(self.qline3.text())
            q4 = int(self.qline4.text())
            result = self.calculate(q1, q2, q3, q4)
            total = format(result, '.2f')
            self.qlabel1.setText(str(total))

    def calculate(self, p, r, y, n):
        total_number_payment = y * n
        calculated_rate = r / 100 / n
        formula_one = calculated_rate * ((calculated_rate + 1) ** total_number_payment)
        formula_two = ((1 + calculated_rate) ** total_number_payment) - 1
        result = p * (formula_one / formula_two)
        return result


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
