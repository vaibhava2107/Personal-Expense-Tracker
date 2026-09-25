import csv
import os

# Personal Expense Tracker


expenses = []   # List to store all expenses
FILE_NAME = "data/expenses.csv"

def show_menu():
    print("\n========== PERSONAL EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search by Category")
    print("4. Monthly Summary")
    print("5. Category Summary")
    print("6. Delete Expense")
    print("7. Edit Expense")
    print("8. Total Expense Summary")
    print("9. Exit")

def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                expenses.append({
                    "amount": float(row["amount"]),
                    "category": row["category"],
                    "description": row["description"],
                    "date": row["date"]
                })



def save_expenses():
    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["amount", "category", "description", "date"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for expense in expenses:
            writer.writerow(expense)

              


# 1. Add Expense
def add_expense():
    while True:
        try:
            amount = float(input("Enter amount (₹): "))
            if amount > 0:
                break
            print("Amount must be greater than 0.")
        except ValueError:
            print("Enter a valid number.")

    category = input("Enter category: ")
    description = input("Enter description: ")

    while True:
        date = input("Enter date (YYYY-MM-DD): ")
        if len(date) == 10 and date[4] == "-" and date[7] == "-":
            break
        print("Use format: YYYY-MM-DD")

    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    expenses.append(expense)
    save_expenses()
    print("Expense added successfully!")


# 2. View Expenses
def view_expenses():
    print("\n========== ALL EXPENSES ==========")

    if len(expenses) == 0:
        print("No expenses found.")
    else:
        for i, expense in enumerate(expenses, start=1):
            print("\n----------------------------------------")
            print(f"Expense No : {i}")
            print(f"Amount     : ₹{expense['amount']}")
            print(f"Category   : {expense['category']}")
            print(f"Description: {expense['description']}")
            print(f"Date       : {expense['date']}")
            print("----------------------------------------")

    input("\nPress Enter to return to the main menu...")


# 3. Search by Category
def search_category():
    category = input("Enter category to search: ")

    found = False
    for expense in expenses:
        if expense["category"].lower() == category.lower():
            print(f"₹{expense['amount']} | {expense['description']} | {expense['date']}")
            found = True

        if not found:
            print("No expenses found in this category.")

input("\nPress Enter to return to the main menu...")


# 4. Monthly Summary
def monthly_summary():
    month = input("Enter month (YYYY-MM): ")

    total = 0
    found = False

    print("\n------ Monthly Expenses ------")

    for expense in expenses:
        if expense["date"].startswith(month):
            print(f"Amount: ₹{expense['amount']}")
            print(f"Category: {expense['category']}")
            print(f"Description: {expense['description']}")
            print(f"Date: {expense['date']}")
            print("----------------------------")

            total += expense["amount"]
            found = True

    if found:
        print(f"Total Expenses in {month}: ₹{total}")
    else:
        print("No expenses found for this month.")

    input("\nPress Enter to return to the main menu...")

# 5. Category Summary
def category_summary():
    if len(expenses) == 0:
        print("No expenses available.")
    else:
        summary = {}

        for expense in expenses:
            category = expense["category"]
            summary[category] = summary.get(category, 0) + expense["amount"]

        print("\n------ Category Summary ------")
        for category, total in summary.items():
            print(f"{category}: ₹{total}")

    input("\nPress Enter to return to the main menu...")


# 6. Delete Expense
def delete_expense():
    if len(expenses) == 0:
        print("No expenses available.")
        input("\nPress Enter to return to the main menu...")
        return

    print("\n------ All Expenses ------")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. ₹{expense['amount']} | {expense['category']} | {expense['description']}")

    number = int(input("\nEnter expense number to delete: "))

    if 1 <= number <= len(expenses):
        expenses.pop(number - 1)
        print("Expense deleted successfully!")
    else:
        print("Invalid expense number.")

    input("\nPress Enter to return to the main menu...")

# 7. Edit Expenses
    # 7. Edit Expenses

def edit_expense():
    if len(expenses) == 0:
        print("No expenses available.")
        return

    print("\n------ All Expenses ------")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['category']} | ₹{expense['amount']} | {expense['description']}")

    number = int(input("\nEnter expense number to edit: "))

    if 1 <= number <= len(expenses):
        expenses[number - 1]["category"] = input("Enter new category: ")
        save_expenses()
        print("Category updated successfully!")
    else:
        print("Invalid expense number.")

    input("\nPress Enter to return to the main menu...")

# 8. Summary Expenses
def total_summary():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("\n====== TOTAL EXPENSE SUMMARY ======")
    print(f"Total Expenses: ₹{total}")
    print(f"Number of Transactions: {len(expenses)}")

    input("\nPress Enter to return to the main menu...")
    

# Main Program
if __name__ == "__main__":
    load_expenses()

    while True:
        show_menu()
        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_category()

        elif choice == "4":
            monthly_summary()

        elif choice == "5":
            category_summary()

        elif choice == "6":
            delete_expense()

        elif choice == "7":
            edit_expense()

        elif choice == "8":
            total_summary()

        elif choice == "9":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 9.")