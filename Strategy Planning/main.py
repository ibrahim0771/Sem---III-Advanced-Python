# Strategy Pattern Example - Payment System

class CreditCard:
    def pay(self):
        print("Payment made using Credit Card")


class DebitCard:
    def pay(self):
        print("Payment made using Debit Card")


class UPI:
    def pay(self):
        print("Payment made using UPI")


class Payment:
    def __init__(self, method):
        self.method = method

    def make_payment(self):
        self.method.pay()


print("Choose Payment Method")
print("1. Credit Card")
print("2. Debit Card")
print("3. UPI")

option = int(input("Enter Your Choice: "))

if option == 1:
    payment = Payment(CreditCard())
elif option == 2:
    payment = Payment(DebitCard())
elif option == 3:
    payment = Payment(UPI())
else:
    print("Invalid Choice")
    exit()

payment.make_payment()

# output
# Choose Payment Method
# 1. Credit Card
# 2. Debit Card
# 3. UPI
# Enter Your Choice: 3

# Payment made using UPI