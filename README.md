
# Banking System Project

## Overview

This **Banking System Project** is a console-based application designed to simulate a simple banking system. It features both **Admin** and **Client** functionalities, allowing users to manage bank accounts, perform transactions, and manage client details. The project leverages CSV files for data storage and includes the capability to generate PDF reports.

## Features

### General:
- **Login System**: Allows users to log in as either an Admin or Client.
  
### Admin Features:
- Display records.
- Search for specific client records.
- Insert new client records.
- Delete client records.
- Edit client details (e.g., email, phone number, balance, transaction pin).

### Client Features:
- View account types and interest rates (e.g., Recurring Deposit, Forward Deposit, Savings).
- Perform transactions (deposit, withdrawal, and transfers).
  
### Other:
- PDF report generation for records.
- Simple data management using CSV files.

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - `csv`: For handling data storage.
  - `pandas`: For data manipulation and record handling.
  - `reportlab`: For generating PDF reports.
  - `datetime`: For handling time-sensitive data (e.g., transaction time).

## Installation

### Prerequisites
- **Python** (Ensure Python 3.x is installed on your system).

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/banking-system.git
   cd banking-system
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the CSV files (`admin.csv`, `client.csv`, and `transaction.csv`) are present in the project directory.

4. Run the application:
   ```bash
   python main.py
   ```

## Usage

1. **Login Menu**: Choose to log in as either:
   - **Admin**: Manage client records.
   - **Client**: Perform account-related transactions.

2. **Admin Menu**:
   - View, search, and manage client records.
   - Edit client details such as email, name, balance, and transaction pin.

3. **Client Menu**:
   - Check available account types and interest rates.
   - Perform transactions (deposit, withdraw, or transfer).

4. **Report Generation**:
   - Admins can generate PDF reports summarizing account details.

## Project Structure

```
.
├── README.md           # Project Documentation
├── main.py             # Main entry point of the application
├── admin.csv           # CSV file storing admin information
├── client.csv          # CSV file storing client records
├── transaction.csv     # CSV file storing transaction history
├── requirements.txt    # List of Python dependencies
```

## Future Improvements

- Implement a database management system (e.g., MySQL) for improved data handling.
- Add encryption for sensitive information (e.g., passwords, transaction pins).
- Create a GUI for better user interaction.
- Expand the client functionality (e.g., loan management, account statements).



