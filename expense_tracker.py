# Personal Expense Tracker
# This console project helps users add expenses, view them,
# calculate total spending, and see spending by category.
# Expenses are saved in a text file so they are available next time.


class Expense:
    # This class stores one expense.
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category


class ExpenseTracker:
    # This class controls the full expense tracker program.
    def __init__(self):
        self.expenses = []
        self.file_name = "expenses.txt"

    def load_expenses(self):
        try:
            # Open the saved file and load each expense into the list.
            with open(self.file_name, "r") as file:
                for line in file:
                    line = line.strip()
                    data = line.split(",")

                    expense = Expense(data[0], float(data[1]), data[2])
                    self.expenses.append(expense)
        except FileNotFoundError:
            print("No saved expenses found. Starting fresh.")

    def save_expenses(self):
        # Save all expenses to the text file.
        with open(self.file_name, "w") as file:
            for expense in self.expenses:
                file.write(f"{expense.name},{expense.amount},{expense.category}\n")

    def show_menu(self):
        print("\n================================")
        print("     Personal Expense Tracker")
        print("================================")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show total expense")
        print("4. Show category summary")
        print("5. Load sample data")
        print("6. Exit")
        print("--------------------------------")

    def add_expense(self):
        name = input("Enter expense name: ")

        while True:
            try:
                # Convert the input to a number and check if it is valid.
                amount = float(input("Enter expense amount: "))

                if amount < 0:
                    raise ValueError("Expense amount cannot be negative.")

                break
            except ValueError as error:
                print(f"Invalid amount: {error}")

        category = input("Enter expense category: ")

        expense = Expense(name, amount, category)
        self.expenses.append(expense)
        self.save_expenses()
        print("Expense added successfully.")

    def view_expenses(self):
        if len(self.expenses) == 0:
            print("No expenses added yet.")
        else:
            print("\nYour Expenses:")
            for index, expense in enumerate(self.expenses, start=1):
                print(f"{index}. {expense.name} - Rs. {expense.amount} ({expense.category})")

    def total_expense(self):
        total = 0
        for expense in self.expenses:
            total = total + expense.amount
        print(f"Total expense: Rs. {total}")

    def category_summary(self):
        if len(self.expenses) == 0:
            print("No expenses added yet.")
        else:
            # This dictionary stores category names and their total amounts.
            summary = {}

            for expense in self.expenses:
                category = expense.category
                amount = expense.amount

                if category in summary:
                    summary[category] = summary[category] + amount
                else:
                    summary[category] = amount

            print("\nCategory Summary:")
            for category, total in summary.items():
                print(f"{category}: Rs. {total}")

    def load_sample_data(self):
        sample_expenses = [
            Expense("Lunch", 120, "Food"),
            Expense("Bus Ticket", 30, "Travel"),
            Expense("Notebook", 60, "Study"),
            Expense("Tea", 15, "Food")
        ]

        for expense in sample_expenses:
            self.expenses.append(expense)

        self.save_expenses()
        print("Sample data added successfully.")

    def run(self):
        print("Welcome! Track your daily expenses easily.")
        self.load_expenses()

        while True:
            self.show_menu()
            choice = input("Choose an option: ")
            valid_choices = ["1", "2", "3", "4", "5", "6"]

            if choice not in valid_choices:
                print("Invalid choice. Please enter a number from 1 to 6.")
            elif choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.total_expense()
            elif choice == "4":
                self.category_summary()
            elif choice == "5":
                self.load_sample_data()
            elif choice == "6":
                print("Goodbye!")
                break


tracker = ExpenseTracker()
tracker.run()
