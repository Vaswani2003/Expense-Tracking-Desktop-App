import sys
import middleware
from datetime import datetime, timedelta

from PyQt6.QtWidgets import QDialog, QApplication, QMainWindow,QComboBox, QLabel, QLineEdit, QFormLayout, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtCharts import QChart, QChartView, QPieSeries
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_user = None
        self.current_transactions = []
        self.all_transactions = []

        self.setWindowTitle("Expense Tracker")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget(self) 
        self.layout = QVBoxLayout()
        self.list_layout = QVBoxLayout()
        
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.layout)
        self.opening_page()

# ----------------------------------------------------------------------------- Pages ----------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------- Opening Page ----------------------------------------------------------------------------------------------

    def opening_page(self):
        self.clear_layout(self.layout)
        self.setStyleSheet("background-color: #2b2b2b;") 
        self.layout.setContentsMargins(20, 20, 20, 20)

        choose_label = QLabel("Choose between the two", self)
        choose_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  
        choose_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #ffffff;")
        self.layout.addWidget(choose_label)

        button_layout = QHBoxLayout()
        button_layout.setSpacing(20)

        new_user_button = QPushButton("New User", self)
        new_user_button.setStyleSheet("""
            QPushButton {
                background-color: #555555; 
                color: white;
                font-size: 18px;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #666666; 
            }
        """)
        new_user_button.clicked.connect(self.new_user_registration)
        button_layout.addWidget(new_user_button)

        existing_user_button = QPushButton("Existing User", self)
        existing_user_button.setStyleSheet("""
            QPushButton {
                background-color: #555555; 
                color: white;
                font-size: 18px;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #666666; 
            }
        """)
        existing_user_button.clicked.connect(self.existing_user_login)
        button_layout.addWidget(existing_user_button)

        self.layout.addLayout(button_layout)



# ----------------------------------------------------------------------------- New USer Registration Page ----------------------------------------------------------------------------------------------


    def new_user_registration(self):
        self.clear_layout(self.layout)
        self.resize(450, 200)
        self.setStyleSheet("background-color: #2b2b2b;")
        newuser_label = QLabel("New User Registration", self)
        newuser_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        newuser_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #ffffff;")
        self.layout.addWidget(newuser_label)

        form_layout = QFormLayout()
        form_layout.setSpacing(10)  
        form_layout.setContentsMargins(20, 20, 20, 20)  

        name_input = QLineEdit()
        name_input.setStyleSheet("background-color: #444444; color: white; border: 1px solid #555555; padding: 5px;")
        form_layout.addRow("Name", name_input)

        username_input = QLineEdit()
        username_input.setStyleSheet("background-color: #444444; color: white; border: 1px solid #555555; padding: 5px;")
        form_layout.addRow("Username", username_input)

        password_input = QLineEdit()
        password_input.setEchoMode(QLineEdit.EchoMode.Password)
        password_input.setStyleSheet("background-color: #444444; color: white; border: 1px solid #555555; padding: 5px;")
        form_layout.addRow("Password", password_input)

        confirm_password_input = QLineEdit()
        confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        confirm_password_input.setStyleSheet("background-color: #444444; color: white; border: 1px solid #555555; padding: 5px;")
        form_layout.addRow("Confirm Password", confirm_password_input)

        register_button = QPushButton("Register", self)
        register_button.setStyleSheet("""
            QPushButton {
                background-color: #555555;  
                color: white;
                font-size: 18px;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #666666;  
            }
        """)
        register_button.clicked.connect(lambda: self.handle_registration(name_input.text(), username_input.text(), password_input.text(), confirm_password_input.text()))
        form_layout.addWidget(register_button)

        self.layout.addLayout(form_layout)


# ----------------------------------------------------------------------------- Exising User Login  Page ----------------------------------------------------------------------------------------------

    def existing_user_login(self):
        self.clear_layout(self.layout)
        self.resize(450, 200)
        self.setStyleSheet("background-color: #2b2b2b;")
        
        existing_user_label = QLabel("Existing User Login", self)
        existing_user_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        existing_user_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #ffffff;")
        self.layout.addWidget(existing_user_label)

        form_layout = QFormLayout()
        form_layout.setSpacing(10)
        form_layout.setContentsMargins(20, 20, 20, 20)

        username_input = QLineEdit()
        username_input.setStyleSheet("background-color: #444444; color: white; border: 1px solid #555555; padding: 5px;")
        form_layout.addRow("Username", username_input)

        password_input = QLineEdit()
        password_input.setEchoMode(QLineEdit.EchoMode.Password)
        password_input.setStyleSheet("background-color: #444444; color: white; border: 1px solid #555555; padding: 5px;")
        form_layout.addRow("Password", password_input)

        login_button = QPushButton("Login", self)
        login_button.setStyleSheet("""
            QPushButton {
                background-color: #555555;
                color: white;
                font-size: 18px;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #666666;
            }
        """)
        login_button.clicked.connect(lambda: self.handle_login(username_input.text(), password_input.text()))
        form_layout.addWidget(login_button)

        self.layout.addLayout(form_layout)


# ----------------------------------------------------------------------------- Income Vs Expenses Page ----------------------------------------------------------------------------------------------

    def hero_page(self):
        self.clear_layout(self.layout)
        self.resize(600, 400)
        self.setStyleSheet("background-color: #2b2b2b;")

        hero_label = QLabel("Welcome to Expense Tracker", self)
        hero_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        hero_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #ffffff;")
        self.layout.addWidget(hero_label)

        if self.current_user.income == 0 and self.current_user.expenses == 0:
            nothing_label = QLabel("You have nothing to display!\n Add Income or expense to view data", self)
            nothing_label.setStyleSheet("font-size: 18px; color: #ffffff;")
            self.layout.addWidget(nothing_label)

        else:
            greeting_label = QLabel(f"Hello {self.current_user.name}!", self)
            greeting_label.setStyleSheet("font-size: 18px; color: #ffffff;")
            self.layout.addWidget(greeting_label)

            self.display_income_vs_expenses()

        button_layout = QHBoxLayout()

        add_income_button = QPushButton("Add Income", self)
        add_income_button.setStyleSheet("""
            QPushButton {
                background-color: #555555;
                color: white;
                font-size: 18px;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #666666;
            }
        """)
        add_income_button.clicked.connect(lambda: self.transaction_popup("income"))
        button_layout.addWidget(add_income_button)

        add_expense_button = QPushButton("Add Expense", self)
        add_expense_button.setStyleSheet("""
            QPushButton {
                background-color: #555555;
                color: white;
                font-size: 18px;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #666666;
            }
        """)
        add_expense_button.clicked.connect(lambda: self.transaction_popup("expense"))
        button_layout.addWidget(add_expense_button)

        self.layout.addLayout(button_layout)

        transactions_divider = QHBoxLayout()
        transactions_label = QLabel("View all transactions ", self)
        transactions_label.setStyleSheet("color: #ffffff;")
        transactions_divider.addWidget(transactions_label)

        filter_dropdown = QComboBox(self)
        filter_dropdown.setStyleSheet("background-color: #444444; color: white; border: 1px solid #555555; padding: 5px;")
        filter_dropdown.addItem("All Transactions")
        filter_dropdown.addItem("Income Only")
        filter_dropdown.addItem("Expenses Only")
        filter_dropdown.addItem("Last 7 Days")
        filter_dropdown.addItem("Last 30 Days")
        filter_dropdown.addItem("Sort by Date")
        filter_dropdown.addItem("Sort by Amount")
        self.layout.addWidget(filter_dropdown)
        
        filter_dropdown.currentIndexChanged.connect(self.apply_filter)
        self.layout.addLayout(transactions_divider)

        display = []
        n = len(self.current_transactions)

        if n > 0 and n < 7:
            display += self.current_transactions
        else:
            display = self.current_transactions[:7]

        if n != 0:
            for transaction in display:
                transaction_i = QPushButton(f"• {transaction['amount']} \t Type: {transaction['category']} \t Made by: {transaction['by']}", self)
                self.list_layout.addWidget(transaction_i)

            self.layout.addLayout(self.list_layout)



    def transaction_popup(self, transaction_type):
        dialog = QDialog(self)
        dialog.setWindowTitle(f"Add {transaction_type}")
        dialog.setStyleSheet("background-color: #2b2b2b; color: #ffffff;")

        form_layout = QVBoxLayout()
        form_layout.setSpacing(10)

        amount_label = QLabel("Amount:", dialog)
        amount_label.setStyleSheet("color: #ffffff;")
        form_layout.addWidget(amount_label)
        
        amount_input = QLineEdit(dialog)
        amount_input.setStyleSheet("background-color: #444444; color: white; border: 1px solid #555555; padding: 5px;")
        form_layout.addWidget(amount_input)

        description_label = QLabel("Description:", dialog)
        description_label.setStyleSheet("color: #ffffff;")
        form_layout.addWidget(description_label)
        
        description_input = QLineEdit(dialog)
        description_input.setStyleSheet("background-color: #444444; color: white; border: 1px solid #555555; padding: 5px;")
        form_layout.addWidget(description_input)

        button_layout = QHBoxLayout()
        
        submit_button = QPushButton("Submit", dialog)
        submit_button.setStyleSheet("""
            QPushButton {
                background-color: #555555;
                color: white;
                font-size: 18px;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #666666;
            }
        """)
        submit_button.clicked.connect(lambda: self.trigger_transaction(dialog, self.current_user.username, transaction_type, amount_input.text(), description_input.text()))
        button_layout.addWidget(submit_button)

        cancel_button = QPushButton("Cancel", dialog)
        cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #555555;
                color: white;
                font-size: 18px;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #666666;
            }
        """)
        cancel_button.clicked.connect(dialog.reject)
        button_layout.addWidget(cancel_button)

        form_layout.addLayout(button_layout)
        dialog.setLayout(form_layout)
        dialog.exec()

# ----------------------------------------------------------------------------- End of Pages ----------------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------- Helper Functions ----------------------------------------------------------------------------------------------


    def handle_login(self, username, password):
        
        success = middleware.login(username, password)

        if success.code == 200:
            print("Login successful")
            self.clear_layout(self.layout)
            self.current_user = success.load
            self.current_transactions = middleware.get_transactions(username)
            self.all_transactions = self.current_transactions
            self.hero_page()

        elif success.code == 401:
            print("Login Failed!, Invalid Credentials")
            invalid_credentials_label = QLabel("Invalid Credentials", self)
            self.layout.addWidget(invalid_credentials_label)

        elif success.code == 402:
            print("Login Failed!, User does not exist")
            user_not_found_label = QLabel("User does not exist", self)
            self.layout.addWidget(user_not_found_label)
        
        elif success.code == 500:
            print("Login Failed!, Error connecting to DB")
            error_label = QLabel("Error connecting to DB", self)
            self.layout.addWidget(error_label)


    def handle_registration(self, name, username, password, confirm_password):

        success = middleware.new_user_registration(name, username, password, confirm_password)

        if success.code == 200:
            print("User registered successfully")
            self.clear_layout(self.layout)
            self.current_user = success.load
            self.current_transactions = middleware.get_transactions(username)
            self.all_transactions = self.current_transactions
            self.hero_page()

        elif success.code == 401:
            print("Registration Failed!, Passwords do not match")
            password_mismatch_label = QLabel("Passwords do not match", self)
            self.layout.addWidget(password_mismatch_label)

        elif success.code == 402:
            print("Registration Failed!, Username already exists")
            username_exists_label = QLabel("Username already exists", self)
            self.layout.addWidget(username_exists_label)

        elif success.code == 500:
            print("Registration Failed!, Error connecting to DB")
            error_label = QLabel("Error connecting to DB", self)
            self.layout.addWidget(error_label)

        elif success.code == 501:
            print("Registration Failed!, Invalid Username")
            invalid_username_label = QLabel("Invalid Username", self)
            self.layout.addWidget(invalid_username_label)

    # def transaction_popup(self, transaction_type):
    #     dialog = QDialog(self)
    #     dialog.setWindowTitle(f"Add {transaction_type}")

    #     form_layout = QVBoxLayout()
    #     form_layout.setSpacing(10)

    #     amount_label = QLabel("Amount:", dialog)
    #     form_layout.addWidget(amount_label)
    #     amount_input = QLineEdit(dialog)
    #     form_layout.addWidget(amount_input)

    #     description_label = QLabel("Description:", dialog)
    #     form_layout.addWidget(description_label)
    #     description_input = QLineEdit(dialog)
    #     form_layout.addWidget(description_input)

    #     button_layout = QHBoxLayout()
    #     submit_button = QPushButton("Submit", dialog)
    #     submit_button.clicked.connect(lambda: self.trigger_transaction(dialog, self.current_user.username, transaction_type, amount_input.text(),description_input.text()))
    #     button_layout.addWidget(submit_button)

    #     cancel_button = QPushButton("Cancel", dialog)
    #     cancel_button.clicked.connect(dialog.reject)
    #     button_layout.addWidget(cancel_button)

    #     form_layout.addLayout(button_layout)
    #     dialog.setLayout(form_layout)
    #     dialog.exec()        

    def trigger_transaction(self,dialog, by, transaction_type, amount, description):
        middleware.create_transaction(by, transaction_type, amount, description)

        if transaction_type == "income":
            self.current_user.income += float(amount)
        else:
            self.current_user.expenses += float(amount)
        
        dialog.accept() 
        self.refresh_list()
        self.hero_page()
        
    def refresh_list(self):
        self.current_transactions = middleware.get_transactions(self.current_user.username)    
        self.all_transactions = self.current_transactions    

    def display_income_vs_expenses(self):
        income = self.current_user.income
        expenses = self.current_user.expenses
        series = QPieSeries()

        series.append(f"Income: {income}", income)
        series.append(f"Expenses: {expenses}", expenses)

        income_slice = series.slices()[0]
        income_slice.setBrush(QColor("green"))
        income_slice.setExploded(True) 
        income_slice.setLabelVisible(True)

        expense_slice = series.slices()[1]
        expense_slice.setBrush(QColor("red"))
        expense_slice.setLabelVisible(True)

        chart = QChart()

        chart.addSeries(series)
        chart.setTitle("Income vs Expenses")
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        chart_view.setFixedSize(500, 350)
  
        self.layout.addWidget(chart_view)


    def apply_filter(self, index):
    
        selected_filter = {
            0: "All Transactions",
            1: "Income Only",
            2: "Expenses Only",
            3: "Last 7 Days",
            4: "Last 30 Days",
            5: "Sort by Date",
            6: "Sort by Amount"
        }

        filter_name = selected_filter.get(index)
        print(f"Filter applied: {filter_name}")
        self.update_filtered_transactions(filter_name)


    def update_filtered_transactions(self, filter_name):
        if filter_name == "All Transactions":
            self.current_transactions = self.all_transactions
        elif filter_name == "Income Only":
            self.current_transactions = [transaction for transaction in self.all_transactions if transaction["category"] == "income"]
        elif filter_name == "Expenses Only":
            self.current_transactions = [transaction for transaction in self.all_transactions if transaction["category"] == "expense"]
        elif filter_name == "Last 7 Days":
            self.current_transactions = self.filter_transactions_by_date(days=7)
        elif filter_name == "Last 30 Days":
            self.current_transactions = self.filter_transactions_by_date(days=30)
        elif filter_name == "Sort by Amount":
            self.current_transactions = middleware.sort_transactions_by_amount(self.current_user.username)
        
        self.hero_page()

    def filter_transactions_by_date(self, days):
        cutoff_date = datetime.now() - timedelta(days=days)
        return [transaction for transaction in self.all_transactions if datetime.strptime(transaction["date"], "%Y-%m-%d %H:%M:%S") >= cutoff_date]

    def clear_layout(self, layout): 
        while layout.count() > 0:

            item = layout.takeAt(0)

            if item.widget():
                item.widget().deleteLater() 

            elif item.layout():
                self.clear_layout(item.layout()) 


# ----------------------------------------------------------------------------- Helper Functions ----------------------------------------------------------------------------------------------


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())