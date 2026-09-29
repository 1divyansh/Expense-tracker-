# Expense Tracker

A simple command-line expense tracker written in Python. Add your expenses, sort them into categories, set a budget, and see where your money goes, all from a menu in the terminal.

No libraries to install, no database: just plain Python.

## Features

- **Add expenses** with a name, an amount and a category (Food, Home, Work, Entertainment, Misc)
- **View all expenses** as a numbered list
- **Delete an expense:** asks you to confirm first
- **Summary by category:** total and percentage per category, with a text bar chart
- **Budget tracking:** starts at Rs.5000 and can be changed; after each action you see how much is left, with a warning when you go over

## Requirements

- Python 3.6 or newer
- Nothing else to install

## Getting Started

```bash
git clone https://github.com/1divyansh/Expense-tracker-.git
cd Expense-tracker-
python3 main.py
```

On Windows, use `python main.py` if `python3` isn't recognised.

## Usage

When the app starts, you'll see the main menu:

```
 Main Menu
1. Add Expenses
2. View Expense
3. Delete Expense
4. View Summary
5. Edit Budget
6. Exit
Enter your choice [1 - 6]:
```

Type a number and press Enter.

### Adding an expense

```
Getting User Expenses
Enter expense name: Rent
Enter expense amount: 1200
Select a category:
1. Food
2. Home
3. Work
4. Entertainment
5. Misc
Enter categrory number [1 - 5]: 2
Saving the Expense: Rent (Home) - 1200.0
[] budget: Rs.1000, spent: 1200.0
 [] WARNING: you have exceeded the budget by 200.0
```

### Viewing expenses

```
[] Your Expenses
 1. Rent (Home) - 1200.0
 2. Coffee (Food) - 4.5
```

### Summary by category

```
[] Expenses by category:
 [] Home: 1200.0 (99.62640099626401%) ####################
 [] Food: 4.5 (0.37359900373599003%) #
[] Total spent: 1204.5
```

Each `#` in the bar is about 5% of your total spending.

### Budget

The budget starts at **Rs.5000**. Choose option 5 to change it (whole numbers only). After you add, view, delete or summarise expenses, the app shows your budget status:

```
[] budget: Rs.1000, spent: 1204.5
 [] WARNING: you have exceeded the budget by 204.5
```

### Tips

- When choosing an expense to delete, press **Enter** without typing a number to cancel.
- Choose option **6** to exit and see how many expenses you recorded and your total spending.

## Important: Data Is Not Saved

All expenses are kept **in memory only**. When you exit, everything you entered is gone.

## Project Structure

```
Expense-tracker-/
├── main.py      # Menu loop and all app features
├── expense.py   # NewExpense(): builds one expense dictionary
├── README.md
└── .gitignore
```

### How the code works

Each expense is a plain dictionary, created by `NewExpense()` in `expense.py`:

```python
{"name": "Coffee", "amount": 4.5, "cat": "Food"}
```

`main()` keeps all expenses in a list and runs the menu loop. Each menu option calls its own function:

| Function | What it does |
|---|---|
| `get_expenses()` | Asks for the name, amount and category of a new expense |
| `view_expenses()` | Lists every expense with its number |
| `delete_expense()` | Removes an expense after you confirm |
| `choose_expense()` | Lets you pick an expense by number (used by delete) |
| `summrize()` | Shows totals, percentages and bars for each category |
| `budget_status()` | Shows the budget, amount spent, and remaining or over-budget amount |
| `total_expenses()` | Adds up all the amounts |
| `exit()` | Prints the session summary and says goodbye |

## Ideas for Future Improvements

- Edit an existing expense
- Check every input so a typo can't crash the app, including negative amounts
- Round percentages and format amounts (for example `Rs.1,200.00`)
- Exit cleanly on Ctrl+C
- Let users add their own categories
- An optional date for each expense
