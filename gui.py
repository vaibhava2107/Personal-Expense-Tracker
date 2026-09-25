import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
from PIL import Image, ImageTk
import csv
import os

# CSV FILE
FILE_NAME = "data/expenses.csv"

os.makedirs("data", exist_ok=True)

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["amount", "category", "description", "date"])

# MAIN WINDOW
root = tk.Tk()
root.title("Personal Expense Tracker")
root.geometry("800x550")
root.resizable(False, False)

# BACKGROUND 
img = Image.open("Images/background.png")
img = img.resize((800, 550))
background = ImageTk.PhotoImage(img)

bg = tk.Label(root, image=background)
bg.place(relwidth=1, relheight=1)

# TITLE
title = tk.Label(
    root,
    text="💸 PERSONAL EXPENSE TRACKER",
    font=("Verdana", 20, "bold"),
    bg="#4EA1D3",
    fg="white"
)
title.pack(pady=(20,5))

subtitle = tk.Label(
    root,
    text="Manage your daily expenses easily",
    font=("Arial",11),
    bg="#4EA1D3",
    fg="white"
)
subtitle.pack(pady=(0,20))

# FUNCTIONS

def add_expense():
    win = tk.Toplevel(root)
    win.title("Add Expense")
    win.geometry("350x380")
    win.configure(bg="#EAF6FF")

    tk.Label(win,text="Amount",bg="#EAF6FF",font=("Arial",10,"bold")).pack(pady=5)
    amount = tk.Entry(win,width=30)
    amount.pack()

    tk.Label(win,text="Category",bg="#EAF6FF",font=("Arial",10,"bold")).pack(pady=5)
    category = ttk.Combobox(
        win,
        width=27,
        state="readonly",
        values=[
            "Food","Travel","Shopping","Grocery","Entertainment",
            "Health","Education","Bills","Recharge",
            "Online Shopping","Others"
        ]
    )
    category.current(0)
    category.pack()

    tk.Label(win,text="Description",bg="#EAF6FF",font=("Arial",10,"bold")).pack(pady=5)
    description = tk.Entry(win,width=30)
    description.pack()

    tk.Label(win,text="Date (YYYY-MM-DD)",bg="#EAF6FF",font=("Arial",10,"bold")).pack(pady=5)
    date = tk.Entry(win,width=30)
    date.pack()

    def save():
        if amount.get()=="" or description.get()=="" or date.get()=="":
            messagebox.showerror("Error","Please fill all fields.")
            return

        try:
            value=float(amount.get())
        except:
            messagebox.showerror("Error","Enter a valid amount.")
            return

        with open(FILE_NAME,"a",newline="") as file:
            writer=csv.writer(file)
            writer.writerow([value,category.get(),description.get(),date.get()])

        messagebox.showinfo("Success","Expense added successfully!")
        win.destroy()

    tk.Button(win,text="Save Expense",bg="#2ECC71",fg="white",
              font=("Arial",11,"bold"),width=18,
              command=save).pack(pady=12)

    tk.Button(win,text="⬅ Back",command=win.destroy,bg="white",
              fg="#154360",width=12).pack()


from tkinter import ttk

def view_expenses():
    win = tk.Toplevel(root)
    win.title("View Expenses")
    win.geometry("760x420")
    win.configure(bg="white")

    tk.Label(
        win,
        text="ALL EXPENSES",
        font=("Arial", 16, "bold"),
        bg="white"
    ).pack(pady=10)

    # Table
    columns = ("Date", "Category", "Description", "Amount")

    table = ttk.Treeview(win, columns=columns, show="headings", height=12)

    # Headings
    for col in columns:
        table.heading(col, text=col)

    # Column sizes
    table.column("Date", width=110, anchor="center")
    table.column("Category", width=130, anchor="center")
    table.column("Description", width=280, anchor="w")
    table.column("Amount", width=100, anchor="center")

    # Scrollbar
    scrollbar = ttk.Scrollbar(win, orient="vertical", command=table.yview)
    table.configure(yscrollcommand=scrollbar.set)

    table.pack(side="left", fill="both", expand=True, padx=(15, 0), pady=10)
    scrollbar.pack(side="right", fill="y", pady=10)

    # Read CSV and sort by date (latest first)
    expenses = []

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append(row)

    expenses.sort(key=lambda x: x["date"], reverse=True)

    # Insert rows
    for expense in expenses:
        table.insert("", "end", values=(
            expense["date"],
            expense["category"],
            expense["description"],
            f"₹{expense['amount']}"
        ))

    # Back button
    tk.Button(
        win,
        text="⬅ Back",
        command=win.destroy,
        bg="white",
        fg="black",
        font=("Arial", 10, "bold"),
        width=12
    ).pack(pady=10)


from tkinter import ttk

def search_category():
    win = tk.Toplevel(root)
    win.title("Search by Category")
    win.geometry("420x420")
    win.configure(bg="#EAF6FF")

    tk.Label(
        win,
        text="Search Expenses by Category",
        font=("Arial", 14, "bold"),
        bg="#EAF6FF"
    ).pack(pady=10)

    tk.Label(
        win,
        text="Select Category",
        font=("Arial", 10, "bold"),
        bg="#EAF6FF"
    ).pack()

    # Predefined category menu
    category = ttk.Combobox(
        win,
        width=25,
        state="readonly",
        values=[
            "Food",
            "Travel",
            "Shopping",
            "Grocery",
            "Entertainment",
            "Health",
            "Education",
            "Bills",
            "Recharge",
            "Online Shopping",
            "Others"
        ]
    )
    category.current(0)
    category.pack(pady=8)

    result_box = tk.Listbox(win, width=55, height=10, font=("Arial", 10))
    result_box.pack(pady=10)

    def search():
        result_box.delete(0, tk.END)
        found = False

        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["category"] == category.get():
                    result_box.insert(
                        tk.END,
                        f"{row['date']} | ₹{row['amount']} | {row['description']}"
                    )
                    found = True

        if not found:
            result_box.insert(tk.END, "No expenses found in this category.")

    tk.Button(
        win,
        text="Search",
        command=search,
        bg="white",
        fg="black",
        font=("Arial", 10, "bold"),
        width=15
    ).pack(pady=5)

    tk.Button(
        win,
        text="⬅ Back",
        command=win.destroy,
        bg="white",
        fg="black",
        font=("Arial", 10, "bold"),
        width=15
    ).pack(pady=8)


def monthly_summary():
    month=simpledialog.askstring("Monthly Summary","Enter Month (YYYY-MM)")
    if not month:
        return

    total=0
    count=0

    with open(FILE_NAME,"r") as file:
        reader=csv.DictReader(file)
        for row in reader:
            if row["date"].startswith(month):
                total+=float(row["amount"])
                count+=1

    messagebox.showinfo(
        "Monthly Summary",
        f"Month : {month}\n\nTransactions : {count}\nTotal Expense : ₹{total}"
    )


def category_summary():
    summary={}

    with open(FILE_NAME,"r") as file:
        reader=csv.DictReader(file)
        for row in reader:
            summary[row["category"]]=summary.get(row["category"],0)+float(row["amount"])

    text=""
    for cat,amt in summary.items():
        text+=f"{cat} : ₹{amt}\n"

    messagebox.showinfo("Category Summary",text if text else "No Expenses")


def total_summary():
    total=0
    count=0

    with open(FILE_NAME,"r") as file:
        reader=csv.DictReader(file)
        for row in reader:
            total+=float(row["amount"])
            count+=1

    messagebox.showinfo(
        "Total Expense Summary",
        f"Total Expenses : ₹{total}\n\nTransactions : {count}"
    )


def edit_expense():

    win = tk.Toplevel(root)
    win.title("Edit Expense")
    win.geometry("760x500")
    win.configure(bg="white")

    tk.Label(
        win,
        text="EDIT EXPENSE",
        font=("Arial",16,"bold"),
        bg="white"
    ).pack(pady=10)

    tk.Label(
        win,
        text="Select an expense to edit",
        bg="white",
        font=("Arial",10)
    ).pack()

    expenses = []

    # Listbox + Scrollbar
    frame = tk.Frame(win, bg="white")
    frame.pack(pady=8)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    listbox = tk.Listbox(
        frame,
        width=85,
        height=8,
        yscrollcommand=scrollbar.set,
        font=("Arial",10)
    )

    listbox.pack(side="left")
    scrollbar.config(command=listbox.yview)

    # Load expenses
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            expenses.append(row)
            listbox.insert(
                tk.END,
                f"{row['date']} | ₹{row['amount']} | {row['category']} | {row['description']}"
            )

    # ---------- Edit Form ----------
    form = tk.Frame(win, bg="white")
    form.pack(pady=15)

    tk.Label(form,text="Amount",bg="white").grid(row=0,column=0,padx=10,pady=6,sticky="w")
    amount_entry = tk.Entry(form,width=25)
    amount_entry.grid(row=0,column=1)

    tk.Label(form,text="Category",bg="white").grid(row=1,column=0,padx=10,pady=6,sticky="w")

    category_box = ttk.Combobox(
        form,
        width=22,
        state="readonly",
        values=[
            "Food","Travel","Shopping","Grocery",
            "Entertainment","Health","Education",
            "Bills","Recharge","Online Shopping","Others"
        ]
    )
    category_box.grid(row=1,column=1)
    category_box.current(0)

    tk.Label(form,text="Description",bg="white").grid(row=2,column=0,padx=10,pady=6,sticky="w")
    description_entry = tk.Entry(form,width=25)
    description_entry.grid(row=2,column=1)

    tk.Label(form,text="Date (YYYY-MM-DD)",bg="white").grid(row=3,column=0,padx=10,pady=6,sticky="w")
    date_entry = tk.Entry(form,width=25)
    date_entry.grid(row=3,column=1)

    # ---------- Load selected expense ----------
    def load_selected(event):
        if not listbox.curselection():
            return

        index = listbox.curselection()[0]
        expense = expenses[index]

        amount_entry.delete(0, tk.END)
        amount_entry.insert(0, expense["amount"])

        category_box.set(expense["category"])

        description_entry.delete(0, tk.END)
        description_entry.insert(0, expense["description"])

        date_entry.delete(0, tk.END)
        date_entry.insert(0, expense["date"])

    listbox.bind("<<ListboxSelect>>", load_selected)

    # ---------- Save Changes ----------
    def save_changes():

        if not listbox.curselection():
            messagebox.showerror("Error","Please select an expense.")
            return

        index = listbox.curselection()[0]

        expenses[index]["amount"] = amount_entry.get()
        expenses[index]["category"] = category_box.get()
        expenses[index]["description"] = description_entry.get()
        expenses[index]["date"] = date_entry.get()

        with open(FILE_NAME,"w",newline="") as file:
            fieldnames = ["amount","category","description","date"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(expenses)

        messagebox.showinfo("Success","Expense updated successfully!")
        win.destroy()

    # Buttons
    tk.Button(
        win,
        text="Save Changes",
        command=save_changes,
        bg="white",
        fg="black",
        font=("Arial",10,"bold"),
        width=18
    ).pack(pady=8)

    tk.Button(
        win,
        text="⬅ Back",
        command=win.destroy,
        bg="white",
        fg="black",
        font=("Arial",10,"bold"),
        width=12
    ).pack()

    
    def update():
        if not listbox.curselection():
            messagebox.showerror("Error", "Select an expense first.")
            return

        index = listbox.curselection()[0]

        # New category dropdown
        new_category = category.get()
        new_description = description.get()

        expenses[index]["category"] = new_category
        expenses[index]["description"] = new_description

        # Save updated CSV
        with open(FILE_NAME, "w", newline="") as file:
            fieldnames = ["amount", "category", "description", "date"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(expenses)

        messagebox.showinfo("Success", "Expense updated successfully.")
        win.destroy()

    tk.Label(win, text="New Category", bg="white",
             font=("Arial", 10, "bold")).pack()

    category = ttk.Combobox(
        win,
        width=25,
        state="readonly",
        values=[
            "Food", "Travel", "Shopping", "Grocery",
            "Entertainment", "Health", "Education",
            "Bills", "Recharge", "Online Shopping", "Others"
        ]
    )
    category.current(0)
    category.pack(pady=5)

    tk.Label(win, text="New Description", bg="white",
             font=("Arial", 10, "bold")).pack()

    description = tk.Entry(win, width=35)
    description.pack(pady=5)

    tk.Button(
        win,
        text="Save Changes",
        command=update,
        bg="white",
        fg="black",
        font=("Arial", 10, "bold"),
        width=15
    ).pack(pady=8)

    tk.Button(
        win,
        text="⬅ Back",
        command=win.destroy,
        bg="white",
        fg="black",
        font=("Arial", 10, "bold"),
        width=15
    ).pack()


def delete_expense():
    messagebox.showinfo(
        "Delete Expense",
        "GUI Delete can be added later. Use main.py for deleting expenses."
    )

# ---------------- MENU ----------------
menu_frame=tk.Frame(root,bg="#4EA1D3")
menu_frame.pack()

btn_style={
    "font":("Arial",10,"bold"),
    "width":18,
    "height":2,
    "bg":"white",
    "fg":"#154360",
    "relief":"raised",
    "bd":1,
    "cursor":"hand2",
    "activebackground":"#EAF6FF"
}

# Row 1
tk.Button(menu_frame,text="➕ Add Expense",command=add_expense,**btn_style).grid(row=0,column=0,padx=10,pady=8)
tk.Button(menu_frame,text="📋 View Expenses",command=view_expenses,**btn_style).grid(row=0,column=1,padx=10,pady=8)

# Row 2
tk.Button(menu_frame,text="🔍 Search Category",command=search_category,**btn_style).grid(row=1,column=0,padx=10,pady=8)
tk.Button(menu_frame,text="📅 Monthly Summary",command=monthly_summary,**btn_style).grid(row=1,column=1,padx=10,pady=8)

# Row 3
tk.Button(menu_frame,text="📊 Category Summary",command=category_summary,**btn_style).grid(row=2,column=0,padx=10,pady=8)
tk.Button(menu_frame,text="💰 Total Summary",command=total_summary,**btn_style).grid(row=2,column=1,padx=10,pady=8)

# Row 4
tk.Button(menu_frame,text="✏ Edit Expense",command=edit_expense,**btn_style).grid(row=3,column=0,padx=10,pady=8)
tk.Button(menu_frame,text="🗑 Delete Expense",command=delete_expense,**btn_style).grid(row=3,column=1,padx=10,pady=8)

# Exit Button
tk.Button(
    root,
    text="🚪 Exit",
    command=root.destroy,
    bg="white",
    fg="#B22222",
    font=("Arial",11,"bold"),
    width=20,
    height=2,
    relief="raised",
    bd=1,
    cursor="hand2"
).pack(pady=18)

root.mainloop()
