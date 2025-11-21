import csv
import os

FILE_NAME = "expenses.csv"

# Create file if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Amount", "Category", "Note"])

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, Shopping, etc.): ")
    note = input("Enter note (optional): ")

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([amount, category, note])

    print("✅ Expense added successfully!")


def view_expenses():
    print("\n📄 All Expenses:")
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


def total_expense():
    total = 0
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            total += float(row[0])
    print(f"\n💰 Total Spent: {total}")


def filter_by_category():
    cat = input("Enter category to filter: ")
    print(f"\n🔎 Expenses under '{cat}':")

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader)
        found = False

        for row in reader:
            if row[1].lower() == cat.lower():
                print(row)
                found = True

        if not found:
            print("❌ No expenses found in this category.")


def expense_tracker():
    while True:
        print("\n📊 EXPENSE TRACKER")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expense")
        print("4. Filter by Category")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            filter_by_category()
        elif choice == "5":
            print("👋 Exiting Expense Tracker...")
            break
        else:
            print("⚠️ Invalid choice. Try again!")


# Run the program
expense_tracker()
