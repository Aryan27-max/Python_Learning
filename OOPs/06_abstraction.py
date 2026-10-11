# Abstraction shows the important action without exposing every detail.
# Both payment types provide a pay() method, but work differently.

class UpiPayment:
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")


class CardPayment:
    def pay(self, amount):
        print(f"Paid ₹{amount} using a card.")


def checkout(payment_method, amount):
    payment_method.pay(amount)


checkout(UpiPayment(), 500)
checkout(CardPayment(), 750)
