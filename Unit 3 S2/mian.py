import csv
import sys

filename = sys.argv[1]

with open(filename, "r") as file:
    groceries = list(csv.DictReader(file))

print("Grocery Items:")
for item in groceries:
    print(item)

item_id = input("Enter Item ID to search: ")

found = False
for item in groceries:
    if item["Item ID"] == item_id:
        print("Item Details:")
        for key, value in item.items():
            print(key + ":", value)
        found = True
        break

if not found:
    print("Item not found.")