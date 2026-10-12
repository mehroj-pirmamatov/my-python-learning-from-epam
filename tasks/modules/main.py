
from expenses import add_expense, remove_expense, get_expenses
from reports import (
    calculate_total,
    expenses_by_category,
    find_largest_expense,
    calculate_average,
    count_by_category,
)


def display_report():
    """Display a complete report of recorded expenses."""
    expenses = get_expenses()

    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n" + "=" * 40)
    print("          EXPENSE REPORT")
    print("=" * 40)

    print(f"Total expenses: {calculate_total(expenses):,.2f}")
    print(f"Number of expenses: {len(expenses)}")
    print(f"Average expense: {calculate_average(expenses):,.2f}")

    print("\nExpenses by category:")
    category_totals = expenses_by_category(expenses)
    category_counts = count_by_category(expenses)

    for category, total in sorted(category_totals.items()):
        print(
            f"  {category}: {total:,.2f} "
            f"({category_counts[category]} expenses)"
        )

    largest = find_largest_expense(expenses)

    print("\nLargest expense:")
    print(f"  Name: {largest['name']}")
    print(f"  Category: {largest['category']}")
    print(f"  Amount: {largest['amount']:,.2f}")
    print("=" * 40)


def main():
    """Run the Expense Tracker application."""
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Remove expense")
        print("4. View expense report")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            name = input("Expense name: ").strip()
            category = input("Category: ").strip()
            amount_text = input("Amount: ").strip()

            try:
                amount = float(amount_text)
                expense = add_expense(name, category, amount)
                print(f"Expense added successfully: {expense}")

            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "2":
            expenses = get_expenses()

            if not expenses:
                print("No expenses recorded yet.")
                continue

            print("\n--- All Expenses ---")

            for index, expense in enumerate(expenses, start=1):
                print(
                    f"{index}. {expense['name']} | "
                    f"{expense['category']} | "
                    f"{expense['amount']:,.2f}"
                )

        elif choice == "3":
            expenses = get_expenses()

            if not expenses:
                print("No expenses available to remove.")
                continue

            for index, expense in enumerate(expenses, start=1):
                print(
                    f"{index}. {expense['name']} - "
                    f"{expense['amount']:,.2f}"
                )

            try:
                index = int(input("Enter expense number to remove: "))
                removed = remove_expense(index - 1)
                print(f"Removed successfully: {removed['name']}")

            except ValueError:
                print("Error: Please enter a valid whole number.")

            except IndexError as error:
                print(f"Error: {error}")

        elif choice == "4":
            display_report()

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid option. Please choose from 1 to 5.")


if __name__ == "__main__":
    main()
