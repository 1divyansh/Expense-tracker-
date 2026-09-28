def main():
    print("Expense Tracker!")

    expenses = []

    while True:
        print("\nMain Menu")
        print("1. Add an expense")
        print("2. View expenses")
        print("3. Exit")

        choice = input("Enter your choice [1 - 3]: ").strip()

        if choice == "1":
            expense = get_user_expenses()
            save_expense(expense, expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            exit_menu(expenses)
            break
        else:
            print("Invalid choice. Please try again!")


def get_user_expenses():
    print("Getting User Expenses")
    expense_name = input("Enter expense name: ")

    while True:
        try:
            expense_amount = float(input("Enter expense amount: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a number!")

    categories = [
        "Food",
        "Home",
        "Work",
        "Entertainment",
        "Misc"
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(categories):
            print(f"{i+1}. {category_name}")

        try:
            category_index = int(input(f"Enter category number [1 - {len(categories)}]: ")) - 1
        except ValueError:
            print("Invalid category. Please try again!")
            continue

        if category_index in range(len(categories)):
            new_expense = {
                "name": expense_name,
                "category": categories[category_index],
                "amount": expense_amount
            }
            return new_expense
        else:
            print("Invalid category. Please try again!")


def save_expense(expense, expenses):
    print(f"Saving the Expense: {expense['name']} ({expense['category']}) - ${expense['amount']:.2f}")
    expenses.append(expense)


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("Your Expenses:")
    total = 0
    for i, expense in enumerate(expenses):
        print(f"{i+1}. {expense['name']} ({expense['category']}) - ${expense['amount']:.2f}")
        total += expense["amount"]
    print(f"Total spent: ${total:.2f}")


def exit_menu(expenses):
    print(f"You recorded {len(expenses)} expense(s) this session.")
    print("Goodbye!")


if __name__ == "__main__":
    main()
