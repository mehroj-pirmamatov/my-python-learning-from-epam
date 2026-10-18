class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")

        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")

        if amount > self.__balance:
            raise ValueError("Insufficient funds.")

        self.__balance -= amount

    def get_balance(self):
        return self.__balance


def main():
    account = BankAccount("Ali", 1000)

    account.deposit(500)
    account.withdraw(200)

    print(f"Account owner: {account.owner}")
    print(f"Current balance: ${account.get_balance()}")


if __name__ == "__main__":
    main()
