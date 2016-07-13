import sys
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QGroupBox, QLineEdit, QLabel, QDesktopWidget


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Resize widget's window screen
        self.resize(600, 200)
        # Set Window Title
        self.setWindowTitle("Loan Calculator")
        # Centers the widget's window screen
        self.center_window_widget()

        grid = QGridLayout()
        grid.addWidget(self.input_fields_group(), 0, 0)
        grid.addWidget(self.output_calculated_group(), 0, 1)
        self.setLayout(grid)

        self.qline1.textEdited.connect(self.text_updated)
        self.qline2.textEdited.connect(self.text_updated)
        self.qline3.textEdited.connect(self.text_updated)
        self.qline4.textEdited.connect(self.text_updated)

    def input_fields_group(self):
        self.input_fields_group_box = QGroupBox("User Input Fields")
        self.loan_amount_label = QLabel("Loan Amount: ")
        self.interest_rate_label = QLabel("Interest Rates (%): ")
        self.number_of_years_label = QLabel("Number of Years: ")
        self.number_of_payment_per_year_label = QLabel("No. of Payments Per Year: ")

        self.qline1 = QLineEdit()
        self.qline1.setValidator(QDoubleValidator(0.0, 999999.99, 2))
        self.qline2 = QLineEdit()
        self.qline2.setValidator(QDoubleValidator(0.0, 999999.99, 2))
        self.qline3 = QLineEdit()
        self.qline3.setValidator(QIntValidator())
        self.qline4 = QLineEdit()
        self.qline4.setValidator(QIntValidator())

        self.qline1.setPlaceholderText("Enter the Loan Amount")
        #self.qlabel1 = QLabel()

        input_gridbox = QGridLayout()

        input_gridbox.addWidget(self.loan_amount_label, 0, 0)
        input_gridbox.addWidget(self.interest_rate_label, 1, 0)
        input_gridbox.addWidget(self.number_of_years_label, 2, 0)
        input_gridbox.addWidget(self.number_of_payment_per_year_label, 3, 0)
        input_gridbox.addWidget(self.qline1, 0, 1)
        input_gridbox.addWidget(self.qline2, 1, 1)
        input_gridbox.addWidget(self.qline3, 2, 1)
        input_gridbox.addWidget(self.qline4, 3, 1)
        #input_gridbox.addWidget(self.qlabel1, 4, 1)

        self.input_fields_group_box.setLayout(input_gridbox)
        return self.input_fields_group_box

    def output_calculated_group(self):
        self.output_calculated_group_box = QGroupBox("Loan Calculations")
        self.scheduled_payment_amount_label = QLabel("Payment Amount: ")
        self.total_number_of_payments_label = QLabel("Total No. of Payments: ")
        self.total_payment_amount_label = QLabel("Total Payment Amount: ")
        self.total_interest_paid_label = QLabel("Total Interest Paid: ")

        self.scheduled_payment_amount = QLineEdit()
        self.total_number_of_payments = QLineEdit()
        self.total_payment_amount = QLineEdit()
        self.total_interest_paid = QLineEdit()
        self.scheduled_payment_amount.setReadOnly(True)
        self.total_number_of_payments.setReadOnly(True)
        self.total_payment_amount.setReadOnly(True)
        self.total_interest_paid.setReadOnly(True)

        output_gridbox = QGridLayout()

        output_gridbox.addWidget(self.scheduled_payment_amount_label, 0, 0)
        output_gridbox.addWidget(self.total_number_of_payments_label, 1, 0)
        output_gridbox.addWidget(self.total_payment_amount_label, 2, 0)
        output_gridbox.addWidget(self.total_interest_paid_label, 3, 0)
        output_gridbox.addWidget(self.scheduled_payment_amount, 0, 1)
        output_gridbox.addWidget(self.total_number_of_payments, 1, 1)
        output_gridbox.addWidget(self.total_payment_amount, 2, 1)
        output_gridbox.addWidget(self.total_interest_paid, 3, 1)

        self.output_calculated_group_box.setLayout(output_gridbox)
        return self.output_calculated_group_box

    def text_updated(self):
        if self.qline1.text() and self.qline2.text() and self.qline3.text() and self.qline4.text():
            print('yes')
            q1 = float(self.qline1.text())
            q2 = float(self.qline2.text())
            q3 = int(self.qline3.text())
            q4 = int(self.qline4.text())
            result = self.calculate(q1, q2, q3, q4)
            total = format(result, '.2f')
            self.scheduled_payment_amount.setText(str(total))

    def calculate(self, p, r, y, n):
        total_number_payment = y * n
        calculated_rate = r / 100 / n
        formula_one = calculated_rate * ((calculated_rate + 1) ** total_number_payment)
        formula_two = ((1 + calculated_rate) ** total_number_payment) - 1
        result = p * (formula_one / formula_two)
        return result

    # Function that centers widget's window on display screen
    def center_window_widget(self):
        window_screen = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        window_screen.moveCenter(center_point)
        self.move(window_screen.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
