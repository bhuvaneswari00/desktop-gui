from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,
    QMessageBox, QTableWidget, QTableWidgetItem
)
from database import Database

class BillingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Billing System")
        self.setGeometry(100, 100, 500, 400)

        layout = QVBoxLayout()

        # Input Fields
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Customer Name")
        layout.addWidget(self.name_input)

        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Phone Number")
        layout.addWidget(self.phone_input)

        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Email")
        layout.addWidget(self.email_input)

        self.amount_input = QLineEdit(self)
        self.amount_input.setPlaceholderText("Bill Amount")
        layout.addWidget(self.amount_input)

        # Buttons
        self.add_button = QPushButton("Add Customer & Bill", self)
        self.add_button.clicked.connect(self.add_customer_bill)
        layout.addWidget(self.add_button)

        # Table to Show Bills
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Customer", "Amount", "Date"])
        layout.addWidget(self.table)

        self.load_data()

        self.setLayout(layout)

    def add_customer_bill(self):
        name = self.name_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        amount = self.amount_input.text()

        if name and phone and amount:
            customer_id = self.db.insert_customer(name, phone, email)
            self.db.insert_bill(customer_id, amount)
            QMessageBox.information(self, "Success", "Customer and bill added successfully")
            self.load_data()
        else:
            QMessageBox.warning(self, "Error", "Please fill in all fields")

    def load_data(self):
        self.table.setRowCount(0)
        bills = self.db.fetch_bills()
        for row_idx, bill in enumerate(bills):
            self.table.insertRow(row_idx)
            for col_idx, value in enumerate(bill):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

if __name__ == "__main__":
    app = QApplication([])
    window = BillingApp()
    window.show()
    app.exec()
