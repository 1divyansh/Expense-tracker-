from expense import NewExpense


def main():
    print(f"Expense Tracker!")
    expenses = []
    budget = 5000
    summrize(expenses)

    while True:
        print("------------------------------------------")
        print("\n Main Menu")
        print("1. Add Expenses")
        print("2. View Expense")
        print("3. Delete Expense")
        print("4. View Summary")
        print("5. Edit Budget")
        print("6. Exit")

        inp = input("Enter your choice [1 - 6]: ").strip()
        print("------------------------------------------")

        if inp == "1":
            print("------------------------------------------")
            expense = get_expenses()
            expenses.append(expense)
            print(f"Saving the Expense: {expense_msg(expense)}")
            budget_status(expenses, budget)
        elif inp == "2":
            print("------------------------------------------")
            view_expenses(expenses)
            budget_status(expenses, budget)
        elif inp == "3":
            print("------------------------------------------")
            delete_expense(expenses)
            budget_status(expenses, budget)
        elif inp == "4":
            print("------------------------------------------")
            summrize(expenses)
            budget_status(expenses, budget)
        elif inp == "5":
            print("------------------------------------------")
            budget = int(input("Enter your budget: "))
        elif inp == "6":
            exit(expenses)
            break
        else:
            print("Invalid choice. Please try again!")


def budget_status(expense, budget=5000):
    total = total_expenses(expense)
    print(f"[] budget: Rs.{budget}, spent: {total}")

    if (total > budget):
        print(f" [] WARNING: you have exceeded the budget by {total - budget}")
    else:
        print(f" [] Remaining Budget: {budget - total}")


def view_expenses(expenses):
    if not expenses:
        return print("[] No expenses recorded")
    print("[] Your Expenses")
    for i, expense in enumerate(expenses):
        print(f" {i + 1}. {expense['name']} ({expense['cat']}) - {expense['amount']}")


def expense_msg(expense):
    return f"{expense['name']} ({expense['cat']}) - {expense['amount']}"


def total_expenses(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def delete_expense(expenses):
    if not expenses:
        return print("There is no expense Recorded")
    i = choose_expense(expenses, "delete")
    if not i:
        return

    confirm = input(f"[] Delete {expense_msg(expenses[i])} ? (y/n)").lower().strip()

    if confirm in ("y", "yes"):
        removed = expenses.pop(i)
        print(f"Deleted {expense_msg(removed)}")
    else:
        print("Cancelled.")


def choose_expense(expenses, edit):
    if not expenses:
        return print("No expenses Recorded yet.")
    print(f"Choose which expense to {edit}")
    for i, expense in enumerate(expenses):
        print(f" {i + 1}. {expense['name']} ({expense['cat']}) - {expense['amount']}")
    while True:
        option = input(f"Choose expense number [1 - {len(expenses)}]: ")
        if option == "":
            print("Cancelled.")
            return
        else:
            return int(option) - 1


def get_expenses():
    print("Getting User Expenses")
    name = input("Enter expense name: ")
    ammount = float(input("Enter expense amount: "))

    categories = ["Food", "Home", "Work", "Entertainment", "Misc"]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(categories):
            print(f"{i + 1}. {category_name}")

        category_index = (int(input(f"Enter categrory number [1 - {len(categories)}]: ")) - 1)

        if category_index in range(len(categories)):
            new_expense = NewExpense(
                name=name,
                category=categories[category_index],
                amount=ammount,
            )
            return new_expense
        else:
            print("Invalid category. please try again!")


def summrize(expenses):
    if not expenses:
        return print("No expense Recorded yet.")

    amount_by_cat = {}
    for data in expenses:
        key = data["cat"]
        if key in amount_by_cat:
            amount_by_cat[key] += data["amount"]
        else:
            amount_by_cat[key] = data["amount"]

    total = total_expenses(expenses)

    print("[] Expenses by category:")
    for cat, amount in amount_by_cat.items():
        percent = amount / total * 100
        bar = "#" * max(1, round(percent / 5))
        print(f" [] {cat}: {amount} ({percent}%) {bar}")

    print(f"[] Total spent: {total}")


def exit(expenses):
    print(f"You recorded {len(expenses)} expenses on this run.")
    print(f"Total spent: {total_expenses(expenses)}")
    print("gg goodbye!")


if __name__ == "__main__":
    main()
