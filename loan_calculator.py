import sys
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QSpinBox,
                             QVBoxLayout, QApplication)

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.principle = QLineEdit()
        self.principle.setValidator(QDoubleValidator(-1, 99.99, 2))
        self.rate = QLineEdit()
        self.rate.setValidator(QDoubleValidator(-1, 99.99, 2))
        self.number_of_years = QSpinBox()
        self.number_of_years.setRange(1, 99)
        self.number_of_years.setValue(5)
        self.number_of_payment_per_years = QSpinBox()
        self.number_of_payment_per_years.setRange(1, 99)
        self.number_of_payment_per_years.setValue(12)

        self.label1 = QLabel()

        vbox = QVBoxLayout()
        vbox.addWidget(self.principle)
        vbox.addWidget(self.rate)
        vbox.addWidget(self.number_of_years)
        vbox.addWidget(self.number_of_payment_per_years)
        vbox.addWidget(self.label1)

        self.setLayout(vbox)


        self.principle.editingFinished.connect(self.loan_calculate)
        self.rate.editingFinished.connect(self.loan_calculate)

        self.number_of_years.editingFinished.connect(self.loan_calculate)
        self.number_of_payment_per_years.editingFinished.connect(self.loan_calculate)

        #self.principle.textChanged.connect(self.loan_calculate)
        #self.rate.textChanged.connect(self.loan_calculate)

        self.number_of_years.valueChanged.connect(self.loan_calculate)
        self.number_of_payment_per_years.valueChanged.connect(self.loan_calculate)


        self.setGeometry(600, 400, 400, 400)
        self.setWindowTitle('Test')

    def loan_calculate(self):
        if self.principle.isModified() and self.rate.isModified():


            p = float(self.principle.text())
            r = float(self.rate.text())
            y = int(self.number_of_years.text())
            n = int(self.number_of_payment_per_years.text())

            if r == 0:
                monthly_payment = self.rate_is_zero_calculate(p, y, n)

            else:
                monthly_payment = self.calculate(p, r, y, n)

            self.label1.setText("{:.2f}".format(monthly_payment))


    def rate_is_zero_calculate(self, p, y, n):
        total_number_payment = y * n
        monthly_payment = p / total_number_payment

        return monthly_payment

    def calculate(self, p, r, y, n):
        total_number_payment = y * n
        calculated_rate = r / 100 / n
        formula_one = calculated_rate * ((calculated_rate + 1) ** total_number_payment)
        formula_two = ((1 + calculated_rate) ** total_number_payment) - 1
        monthly_payment = p * (formula_one / formula_two)
        return monthly_payment

#    def calculate(self, text):
#        if text:
#            text = (int(text) * 2)
#            self.line2.setText(str(text))
#        else: self.line2.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

