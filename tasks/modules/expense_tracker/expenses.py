
expenses = []


def add_expense(name, category, amount):
    """
    Add a new expense to the expenses list.

    Args:
        name (str): Name of the expense.
        category (str): Expense category.
        amount (float): Expense amount.

    Returns:
        dict: The newly created expense.

    Raises:
        ValueError: If the name or category is empty,
                    or the amount is not positive.
    """
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Expense name cannot be empty.")

    if not isinstance(category, str) or not category.strip():
        raise ValueError("Category cannot be empty.")

    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
        raise ValueError("Amount must be a number.")

    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    expense = {
        "name": name.strip(),
        "category": category.strip().title(),
        "amount": amount
    }

    expenses.append(expense)
    return expense


def remove_expense(index):
    """
    Remove an expense by its index.

    Args:
        index (int): Zero-based index of the expense.

    Returns:
        dict: The removed expense.

    Raises:
        IndexError: If the index does not exist.
        TypeError: If the index is not an integer.
    """
    if isinstance(index, bool) or not isinstance(index, int):
        raise TypeError("Index must be an integer.")

    if index < 0 or index >= len(expenses):
        raise IndexError("Expense index does not exist.")

    return expenses.pop(index)


def get_expenses():
    """Return a copy of all recorded expenses."""
    return [expense.copy() for expense in expenses]
