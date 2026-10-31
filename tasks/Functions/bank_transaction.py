
def deposit(balance, amount):
    if amount <= 0:
        return "Invalid deposit amount"

    return balance + amount


def withdraw(balance, amount):
    if amount <= 0:
        return "Invalid withdrawal amount"

    if amount > balance:
        return "Insufficient funds"

    return balance - amount


def get_balance(balance):
    return f"Current balance: {balance:,} UZS"


account_balance = 1_000_000

account_balance = deposit(account_balance, 500_000)
account_balance = withdraw(account_balance, 200_000)

print(get_balance(account_balance))
