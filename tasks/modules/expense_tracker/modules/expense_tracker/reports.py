
def calculate_total(expenses):
    """
    Calculate the total amount of all expenses.

    Args:
        expenses (list): List of expense dictionaries.

    Returns:
        int or float: Total expense amount.
    """
    return sum(expense["amount"] for expense in expenses)


def expenses_by_category(expenses):
    """
    Group expenses by category and calculate each category's total.

    Args:
        expenses (list): List of expense dictionaries.

    Returns:
        dict: Total amount spent in each category.
    """
    report = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        report[category] = report.get(category, 0) + amount

    return report


def find_largest_expense(expenses):
    """
    Find the expense with the highest amount.

    Args:
        expenses (list): List of expense dictionaries.

    Returns:
        dict or None: Largest expense, or None if the list is empty.
    """
    if not expenses:
        return None

    return max(expenses, key=lambda expense: expense["amount"])


def calculate_average(expenses):
    """
    Calculate the average expense amount.

    Args:
        expenses (list): List of expense dictionaries.

    Returns:
        float: Average expense amount, or 0 if there are no expenses.
    """
    if not expenses:
        return 0

    return calculate_total(expenses) / len(expenses)


def count_by_category(expenses):
    """
    Count the number of expenses in each category.

    Args:
        expenses (list): List of expense dictionaries.

    Returns:
        dict: Number of expenses in each category.
    """
    counts = {}

    for expense in expenses:
        category = expense["category"]
        counts[category] = counts.get(category, 0) + 1

    return counts
