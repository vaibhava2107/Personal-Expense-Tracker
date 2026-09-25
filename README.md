# Personal Expense Tracker

## About the Project

This project was developed as part of the Python Essentials course to practice basic Python programming concepts through a menu-driven expense tracker. The project helps a user keep track of daily expenses using a command-line menu. The expenses are stored in a CSV file, so they are available even after closing and reopening the program.

The main goal of this project is to practice Python concepts like functions, loops, conditions, lists, dictionaries, and file handling.

## Features

- Add a new expense.
- View all saved expenses.
- Search expenses by category.
- View monthly expense summary.
- View category-wise expense summary.
- Edit an existing expense.
- Delete an expense.
- View total expense summary.
- Save all expenses in a CSV file.

## Tools Used

- Python 3
- Visual Studio Code
- CSV module (built-in Python library)
- OS module (built-in Python library)

## Project Folder Structure

Expense Calculator/

- `main.py` - Main program.
- `README.md` - Project information.
- `data/expenses.csv` - Stores all expense records.

## How to Run the Project

1. Download or clone this repository.
2. Open the project folder in Visual Studio Code.
3. Open the terminal inside VS Code.
4. Run the following command:

```bash
python main.py
```

5. Choose an option from the menu and use the application.

## How the Project Works

- When the program starts, it reads the saved expenses from `expenses.csv`.
- If a new expense is added, it is stored in the list and saved to the CSV file.
- Users can edit or delete expenses, and the CSV file is updated automatically.
- Different summary options calculate expenses based on category, month, or total spending.

## Learning Outcome

By developing this project, I learned how to create a menu-driven Python application, store data in a CSV file, perform CRUD operations (Create, Read, Update, Delete), and use basic input validation for user input.

## Conclusion

This project is a basic expense management system built using Python. It helped me understand how different Python concepts work together in a real application while keeping the project simple and easy to use.
