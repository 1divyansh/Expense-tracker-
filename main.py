from expense import NewExpense

EXPENSE_FILE_PATH = "expenses.csv"


def main():
    print("Expense Tracker!")

    expense = get_user_expenses()
    save_expense(expense, EXPENSE_FILE_PATH)

    exit_menu()


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
            new_expense = NewExpense(name=expense_name, category=categories[category_index], amount=expense_amount)
            return new_expense
        else:
            print("Invalid category. Please try again!")


def save_expense(expense, expense_file_path):
    print(f"Saving the Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def exit_menu():
    print("Goodbye!")


if __name__ == "__main__":
    main()
