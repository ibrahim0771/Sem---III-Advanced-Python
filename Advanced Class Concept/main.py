# Base Class
class AccountDetails:
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.__balance = balance      # Data Hiding (Encapsulation)

    def get_balance(self):
        return self.__balance

    def display_details(self):
        print("Account Holder :", self.holder_name)
        print("Available Balance :", self.__balance)


# Derived Class - Savings Account
class SavingsAccount(AccountDetails):
    def __init__(self, holder_name, balance, interest):
        super().__init__(holder_name, balance)
        self.interest = interest

    # Method Overriding
    def display_details(self):
        super().display_details()
        print("Interest Percentage :", self.interest, "%")


# Derived Class - Current Account
class CurrentAccount(AccountDetails):
    def __init__(self, holder_name, balance, overdraft):
        super().__init__(holder_name, balance)
        self.overdraft = overdraft

    # Method Overriding
    def display_details(self):
        super().display_details()
        print("Maximum Overdraft :", self.overdraft)


# -------- Main Program --------

print("===== Savings Account Details =====")
savings = SavingsAccount("Rahul", 50000, 6.5)
savings.display_details()

print("\n===== Current Account Details =====")
current = CurrentAccount("Priya", 80000, 25000)
current.display_details()

print("\nCurrent Balance in Savings Account :", savings.get_balance())


# Output
# ===== Savings Account Details =====
# Account Holder : Rahul
# Available Balance : 50000
# Interest Percentage : 6.5 %

# ===== Current Account Details =====
# Account Holder : Priya
# Available Balance : 80000
# Maximum Overdraft : 25000

# Current Balance in Savings Account : 50000