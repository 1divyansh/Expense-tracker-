CATEGORIES = [
    "Food",
    "Home",
    "Work",
    "Entertainment",
    "Misc"
]


def main():
    print("Expense Tracker!")

    expenses = []
    budget = None

    try:
        while True:
            print("\nMain Menu")
            print("1. Add an expense")
            print("2. View expenses")
            print("3. Edit an expense")
            print("4. Delete an expense")
            print("5. View summary by category")
            print("6. Set budget")
            print("7. Exit")

            choice = input("Enter your choice [1 - 7]: ").strip()

            if choice == "1":
                expense = get_user_expenses()
                save_expense(expense, expenses)
                show_budget_status(expenses, budget)
            elif choice == "2":
                view_expenses(expenses)
                show_budget_status(expenses, budget)
            elif choice == "3":
                edit_expense(expenses)
                show_budget_status(expenses, budget)
            elif choice == "4":
                delete_expense(expenses)
                show_budget_status(expenses, budget)
            elif choice == "5":
                view_summary(expenses)
                show_budget_status(expenses, budget)
            elif choice == "6":
                budget = set_budget(budget)
                show_budget_status(expenses, budget)
            elif choice == "7":
                exit_menu(expenses)
                break
            else:
                print("Invalid choice. Please try again!")
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C or Ctrl+D: leave cleanly instead of showing an error
        print()
        exit_menu(expenses)


def get_user_expenses():
    print("Getting User Expenses")
    expense_name = get_name("Enter expense name: ")
    expense_amount = get_amount("Enter expense amount: ")
    expense_category = choose_category()

    new_expense = {
        "name": expense_name,
        "category": expense_category,
        "amount": expense_amount
    }
    return new_expense


def get_name(prompt, allow_blank=False):
    while True:
        name = input(prompt).strip()
        if name or allow_blank:
            return name
        print("Name cannot be empty. Please try again!")


def get_amount(prompt, allow_blank=False):
    while True:
        text = input(prompt).strip()
        if allow_blank and text == "":
            return None

        # Accept inputs like "$12.50" or "1,200"
        text = text.replace("$", "").replace(",", "")

        try:
            amount = float(text)
        except ValueError:
            print("Invalid amount. Please enter a number like 12.50")
            continue

        if 0 < amount < float("inf"):
            return amount
        print("Amount must be greater than 0. Please try again!")


def choose_category(allow_blank=False):
    while True:
        print("Select a category: ")
        for i, category_name in enumerate(CATEGORIES):
            print(f"{i+1}. {category_name}")

        text = input(f"Enter category number [1 - {len(CATEGORIES)}]: ").strip()
        if allow_blank and text == "":
            return None

        try:
            category_index = int(text) - 1
        except ValueError:
            print("Invalid category. Please try again!")
            continue

        if category_index in range(len(CATEGORIES)):
            return CATEGORIES[category_index]
        print("Invalid category. Please try again!")


def format_expense(expense):
    return f"{expense['name']} ({expense['category']}) - ${expense['amount']:,.2f}"


def get_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def save_expense(expense, expenses):
    print(f"Saving the Expense: {format_expense(expense)}")
    expenses.append(expense)


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("Your Expenses:")
    for i, expense in enumerate(expenses):
        print(f"{i+1}. {format_expense(expense)}")
    print(f"Total spent: ${get_total(expenses):,.2f}")


def choose_expense(expenses, action):
    if not expenses:
        print("No expenses recorded yet.")
        return None

    print(f"Which expense do you want to {action}?")
    for i, expense in enumerate(expenses):
        print(f"{i+1}. {format_expense(expense)}")

    while True:
        text = input(f"Enter expense number [1 - {len(expenses)}] (or press Enter to cancel): ").strip()
        if text == "":
            print("Cancelled.")
            return None

        try:
            index = int(text) - 1
        except ValueError:
            print("Invalid number. Please try again!")
            continue

        if index in range(len(expenses)):
            return index
        print("Invalid number. Please try again!")


def edit_expense(expenses):
    index = choose_expense(expenses, "edit")
    if index is None:
        return

    expense = expenses[index]
    print(f"Editing: {format_expense(expense)}")
    print("Press Enter to keep the current value.")

    new_name = get_name(f"New name [{expense['name']}]: ", allow_blank=True)
    if new_name:
        expense["name"] = new_name

    new_amount = get_amount(f"New amount [{expense['amount']:,.2f}]: ", allow_blank=True)
    if new_amount is not None:
        expense["amount"] = new_amount

    print(f"Current category: {expense['category']}")
    new_category = choose_category(allow_blank=True)
    if new_category is not None:
        expense["category"] = new_category

    print(f"Updated: {format_expense(expense)}")


def delete_expense(expenses):
    index = choose_expense(expenses, "delete")
    if index is None:
        return

    confirm = input(f"Delete '{format_expense(expenses[index])}'? (y/n): ").strip().lower()
    if confirm in ("y", "yes"):
        removed = expenses.pop(index)
        print(f"Deleted: {format_expense(removed)}")
    else:
        print("Cancelled.")


def view_summary(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    totals = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]

    total = get_total(expenses)

    print("Summary by Category:")
    # Largest category first
    for category, amount in sorted(totals.items(), key=lambda item: item[1], reverse=True):
        percent = amount / total * 100
        bar = "#" * max(1, round(percent / 5))
        print(f"{category:<14} ${amount:>10,.2f}  ({percent:5.1f}%)  {bar}")
    print(f"{'Total':<14} ${total:>10,.2f}")


def set_budget(budget):
    if budget is not None:
        print(f"Current budget: ${budget:,.2f}")

    new_budget = get_amount("Enter your budget (or press Enter to cancel): ", allow_blank=True)
    if new_budget is None:
        print("Budget unchanged.")
        return budget

    print(f"Budget set to ${new_budget:,.2f}")
    return new_budget


def show_budget_status(expenses, budget):
    if budget is None:
        return

    total = get_total(expenses)
    print(f"Budget: ${budget:,.2f} | Spent: ${total:,.2f}")
    if total > budget:
        print(f"WARNING: You are over budget by ${total - budget:,.2f}!")
    else:
        print(f"Remaining: ${budget - total:,.2f}")


def exit_menu(expenses):
    print(f"You recorded {len(expenses)} expense(s) this session.")
    print(f"Total spent: ${get_total(expenses):,.2f}")
    print("Goodbye!")


if __name__ == "__main__":
    main()
