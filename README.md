# XYZ Bank ATM System — OOP in Python

A simple console-based ATM Banking System built in Python to practice and demonstrate core Object-Oriented Programming (OOP) concepts.

This project simulates basic ATM operations like checking balance, depositing/withdrawing money, changing PIN, and viewing a mini statement — all wrapped inside a clean class-based structure.

---

## Features

- PIN-based secure login (with limited attempts before card block)
- Check account balance
- Deposit money
- Withdraw money (with balance validation)
- Change PIN
- Mini statement
- View account details
- Exit option

---

## OOP Concepts Used

| Concept | Where it's used |
|---|---|
| Class & Object | `BankAccount` and `ATM` classes; `atm` object |
| Constructor (`__init__`) | Initializes account number, name, PIN, and balance |
| Encapsulation | `__pin` and `__balance` are private attributes, accessed only via class methods |
| Getter Method | `get_balance()` safely returns private balance |
| Inheritance | `ATM` class inherits from `BankAccount` |
| Polymorphism (Method Overriding) | `display_details()` is overridden in `ATM` class |

---

## Project Structure

```
├── atm_oop.py      # Main source code
└── README.md       # Project documentation
```

---

## How to Run

1. Make sure you have Python 3 installed.
2. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```
3. Navigate to the project folder and run:
   ```bash
   python atm_oop.py
   ```
4. Enter the ATM PIN when prompted (default demo PIN: `1234`) and use the menu to interact with the ATM.

---

## Demo Account (Default)

| Field | Value |
|---|---|
| Account Number | 1234567890 |
| Name | Atharva Mohite |
| PIN | 1234 |
| Balance | ₹50,000 |

Note: This is a demo account hardcoded for learning purposes. Feel free to modify it in the code.

---

## Notes

The code includes detailed inline comments and docstrings explaining why each OOP concept was used (constructor, encapsulation, inheritance, method overriding, etc.) — written while learning, as a personal reference for revision.

---

## Author

Atharva Mohite
B.Tech AIML (CSE) Student
