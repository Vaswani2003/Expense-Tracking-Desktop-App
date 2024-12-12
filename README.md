# Expense Tracker

An intuitive desktop application built with PyQt6 to manage your daily expenses and income efficiently. The Expense Tracker allows users to register, log in, and visualize their financial data through an easy-to-use interface.

## Features

- **User Authentication**: Register as a new user or log in as an existing user.
- **Expense and Income Tracking**: Add, manage, and categorize your income and expenses.
- **Data Visualization**: View your financial summary with income vs expenses charts.
- **Filters and Sorting**: Filter transactions by type (income/expense) or date, and sort them by amount or date.
- **Dark Mode UI**: Modern dark-themed design for a seamless user experience.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/expense-tracker.git
   cd expense-tracker
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.9 or higher installed. Install the required dependencies using pip:
   ```bash
   pip install PyQt6
   ```

3. **Run the Application**:
   ```bash
   python main.py
   ```

## Usage

1. **Launch the Application**:
   Run the `main.py` script to open the Expense Tracker application.

2. **Register or Login**:
   - If you are a new user, click `New User` and fill out the registration form.
   - If you are an existing user, click `Existing User` and log in with your credentials.

3. **Track Finances**:
   - Add income or expense entries using the respective buttons.
   - Filter and sort transactions to view detailed records.

4. **Visualize Data**:
   - View income vs expense charts for a quick financial summary.

## Application Structure

- **MainWindow**: The main interface controller that manages different pages and functionalities.
- **Pages**:
  - Opening Page: Entry point for new or existing users.
  - Registration Page: Allows new users to register.
  - Login Page: Authenticates existing users.
  - Hero Page: Displays the financial summary and provides transaction management options.

## Technologies Used

- **Python**: Core programming language.
- **PyQt6**: Framework for building the graphical user interface.
- **Middleware**: Custom logic for user and transaction management.

## Contribution

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to reach out with suggestions, feedback, or issues by creating a new issue in the repository or contacting the author directly.
