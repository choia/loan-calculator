# Loan Calculator
import sys
from PyQt5.QtGui import (QIntValidator, QDoubleValidator)
from PyQt5.QtWidgets import (QApplication, QGridLayout, QGroupBox, QMenu, QLabel, QLineEdit,
                             QDesktopWidget, QWidget, QPushButton, QVBoxLayout)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.addWidget(self.user_input_fields_group(), 0, 0)
        grid.addWidget(self.fixed_calculations_group(), 0, 1)
        self.setLayout(grid)

        self.setWindowTitle('Loan Calculator')
        self.resize(600, 200)
        self.center()
        self.show()

    def center(self):
        screen = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        screen.moveCenter(center_point)
        self.move(screen.topLeft())

    def user_input_fields_group(self):
        group_box = QGroupBox("User Input Fields")

        loan_amount = QLabel("Loan Amount: ")
        interest_rate = QLabel("Interest Rate (%): ")
        number_of_years = QLabel("Number of Years: ")
        number_of_payment_per_year = QLabel("Number of Payments Per Year: ")

        loan_amount_edit = QLineEdit()
        loan_amount_edit.setValidator(QDoubleValidator())
        #loan_amount_edit.textChanged.connect(self.loan_calculate())
        interest_rate_edit = QLineEdit()
        interest_rate_edit.setValidator(QDoubleValidator(0.1, 99.99, 2))
        number_of_years_edit = QLineEdit()
        number_of_years_edit.setValidator(QIntValidator())
        number_of_years_edit.setMaxLength(3)
        number_of_payment_per_year_edit = QLineEdit()
        number_of_payment_per_year_edit.setValidator(QIntValidator())
        number_of_payment_per_year_edit.setMaxLength(4)

        box = QGridLayout()

        box.addWidget(loan_amount, 0, 0)
        box.addWidget(interest_rate, 1, 0)
        box.addWidget(number_of_years, 2, 0)
        box.addWidget(number_of_payment_per_year, 3, 0)

        box.addWidget(loan_amount_edit, 0, 1)
        box.addWidget(interest_rate_edit, 1, 1)
        box.addWidget(number_of_years_edit, 2, 1)
        box.addWidget(number_of_payment_per_year_edit, 3, 1)

        group_box.setLayout(box)

        return group_box

    def loan_calculate(self, text):
        pass

    def fixed_calculations_group(self):
        group_box = QGroupBox("Fixed Calculations")

        payment_amount = QLabel("Payment Amount: ")
        total_number_of_payment = QLabel("Total No. of Payments: ")
        total_payment_amount = QLabel("Total Payment Amount: ")
        total_interest_paid = QLabel("Total Interest Paid: ")

        payment_amount_edit = QLineEdit()
        total_number_of_payment_edit = QLineEdit()
        total_payment_amount_edit = QLineEdit()
        total_interest_paid_edit = QLineEdit()

        box = QGridLayout()

        box.addWidget(payment_amount, 0, 0)
        box.addWidget(total_number_of_payment, 1, 0)
        box.addWidget(total_payment_amount, 2, 0)
        box.addWidget(total_interest_paid, 3, 0)

        box.addWidget(payment_amount_edit, 0, 1)
        box.addWidget(total_number_of_payment_edit, 1, 1)
        box.addWidget(total_payment_amount_edit, 2, 1)
        box.addWidget(total_interest_paid_edit, 3, 1)

        group_box.setLayout(box)

        return group_box


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

