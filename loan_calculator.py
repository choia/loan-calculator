import sys
from PyQt5.QtGui import QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp
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

        # Construct PyQt Grid layout and add widgets
        grid = QGridLayout()
        grid.addWidget(self.input_fields_group(), 0, 0)
        grid.addWidget(self.output_calculated_group(), 0, 1)
        self.setLayout(grid)

        # Send signal to the slot when line text is edited
        self.loan_amount_edit.textEdited.connect(self.text_updated)
        self.interest_rate_edit.textEdited.connect(self.text_updated)
        self.num_of_years_edit.textEdited.connect(self.text_updated)
        self.num_payment_per_yr_edit.textEdited.connect(self.text_updated)


    def input_fields_group(self):
        # Function for the input fields group
        self.input_fields_group_box = QGroupBox("User Input Fields")
        self.loan_amount_label = QLabel("Loan Amount: ")
        self.interest_rate_label = QLabel("Interest Rate (%): ")
        self.number_of_years_label = QLabel("Number of Years: ")
        self.number_of_payment_per_year_label = QLabel("No. of Payments Per Year: ")

        self.loan_amount_edit = QLineEdit()
        self.loan_amount_edit.setMaxLength(9)
        self.loan_amount_edit.setValidator(QDoubleValidator(0.0, 999999.99, 2))
        self.loan_amount_edit.setPlaceholderText("Enter the Loan Amount")
        self.interest_rate_edit = QLineEdit()
        self.interest_rate_edit.setMaxLength(5)
        self.interest_rate_edit.setValidator(QDoubleValidator(0.0, 999999.99, 3))

        regex_line_edit = QRegExp("^[1-9][0-9]*")
        validator = QRegExpValidator(regex_line_edit)

        self.num_of_years_edit = QLineEdit()
        self.num_of_years_edit.setMaxLength(2)
        self.num_of_years_edit.setValidator(validator)
        self.num_payment_per_yr_edit = QLineEdit()
        self.num_payment_per_yr_edit.setMaxLength(2)
        self.num_payment_per_yr_edit.setValidator(validator)

        input_gbox = QGridLayout()
        input_gbox.addWidget(self.loan_amount_label, 0, 0)
        input_gbox.addWidget(self.interest_rate_label, 1, 0)
        input_gbox.addWidget(self.number_of_years_label, 2, 0)
        input_gbox.addWidget(self.number_of_payment_per_year_label, 3, 0)
        input_gbox.addWidget(self.loan_amount_edit, 0, 1)
        input_gbox.addWidget(self.interest_rate_edit, 1, 1)
        input_gbox.addWidget(self.num_of_years_edit, 2, 1)
        input_gbox.addWidget(self.num_payment_per_yr_edit, 3, 1)

        self.input_fields_group_box.setLayout(input_gbox)
        return self.input_fields_group_box


    def output_calculated_group(self):
        # Function for the loan calculation group
        self.output_calculated_group_box = QGroupBox("Loan Calculation")
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

        output_gbox = QGridLayout()
        output_gbox.addWidget(self.scheduled_payment_amount_label, 0, 0)
        output_gbox.addWidget(self.total_number_of_payments_label, 1, 0)
        output_gbox.addWidget(self.total_payment_amount_label, 2, 0)
        output_gbox.addWidget(self.total_interest_paid_label, 3, 0)
        output_gbox.addWidget(self.scheduled_payment_amount, 0, 1)
        output_gbox.addWidget(self.total_number_of_payments, 1, 1)
        output_gbox.addWidget(self.total_payment_amount, 2, 1)
        output_gbox.addWidget(self.total_interest_paid, 3, 1)

        self.output_calculated_group_box.setLayout(output_gbox)
        return self.output_calculated_group_box


    def text_updated(self):
        # Triggers this function upon signal text fields in input fields are edited
        if self.loan_amount_edit.text() and self.interest_rate_edit.text() \
                and self.num_of_years_edit.text() and self.num_payment_per_yr_edit.text():

            loan_amount = float(self.loan_amount_edit.text())
            interest_rate = float(self.interest_rate_edit.text())
            num_of_years = int(self.num_of_years_edit.text())
            num_payment_per_yr = int(self.num_payment_per_yr_edit.text())

            monthly_payment = self.calculate_monthly_payment(loan_amount, interest_rate, num_of_years, num_payment_per_yr)
            result_monthly_payment = format(monthly_payment, '.2f')

            result_total_number_of_payment = self.calculate_total_number_of_payment(num_of_years, num_payment_per_yr)

            total_payment_amount = self.calculate_total_payment_amount(monthly_payment, result_total_number_of_payment)
            result_total_payment = format(total_payment_amount, '.2f')

            interest_paid = self.calculate_interest_paid(total_payment_amount, loan_amount)
            result_interest_paid = format(interest_paid, '.2f')

            self.scheduled_payment_amount.setText(str('$ ' + result_monthly_payment))
            self.total_number_of_payments.setText(str(result_total_number_of_payment))
            self.total_payment_amount.setText(str('$ ' + result_total_payment))
            self.total_interest_paid.setText(str('$ ' + result_interest_paid))


    def calculate_monthly_payment(self, principal, rate, years, num_payments_per_year):
        # calculates the scheduled monthly payment
        total_number_payment = years * num_payments_per_year
        calculated_rate = rate / 100 / num_payments_per_year
        formula_one = calculated_rate * ((calculated_rate + 1) ** total_number_payment)
        formula_two = ((1 + calculated_rate) ** total_number_payment) - 1
        result = principal * (formula_one / formula_two)
        return result


    def calculate_total_number_of_payment(self, number_of_years, number_of_payment_per_year):
        # Calculates the total number of payment
        return number_of_years * number_of_payment_per_year


    def calculate_total_payment_amount(self, monthly_payment, total_number_of_payment):
        # Calculates the total payment amount
        return monthly_payment * total_number_of_payment


    def calculate_interest_paid(self, total_payment_amount, loan_amount):
        # Calculates the interest paid
        return total_payment_amount - loan_amount


    def center_window_widget(self):
        # Function that centers widget's window on display screen
        window_screen = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        window_screen.moveCenter(center_point)
        self.move(window_screen.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
