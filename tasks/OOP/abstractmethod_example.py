
from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} UZS by card"


class CashPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} UZS in cash"


payments = [
    CardPayment(),
    CashPayment()
]

for payment in payments:
    print(payment.pay(100000))
