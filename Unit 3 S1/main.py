import csv
import re

with open("customers.csv", "r") as file:
    customers = list(csv.DictReader(file))

print("Customer Details:")
for customer in customers:
    print(customer)

account_number = input("Enter account number to search: ")

if not re.fullmatch(r"\d{10}", account_number):
    print("Invalid account number format.")
else:
    found = False
    for customer in customers:
        if customer["Account Number"] == account_number:
            print("Customer Details:")
            for key, value in customer.items():
                print(key + ":", value)
            found = True
            break

    if not found:
        print("Account not found.")