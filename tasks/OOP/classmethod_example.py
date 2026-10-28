
class BankAccount:
    bank_name = "UzPython Bank"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    def show_info(self):
        return (
            f"Owner: {self.owner}, "
            f"Balance: {self.balance}, "
            f"Bank: {self.bank_name}"
        )


account1 = BankAccount("Ali", 500000)
account2 = BankAccount("Vali", 800000)

BankAccount.change_bank_name("Future Bank")

print(account1.show_info())
print(account2.show_info())
