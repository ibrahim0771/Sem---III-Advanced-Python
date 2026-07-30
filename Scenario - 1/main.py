class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def category(self):
        if self.price >= 50000:
            return "Premium"
        elif self.price >= 20000:
            return "Mid-range"
        else:
            return "Budget"

    def display(self):
        print("Brand   :", self.brand)
        print("Model   :", self.model)
        print("Price   :", self.price)
        print("Category:", self.category())
        print()


class Store:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, mobile):
        self.mobiles.append(mobile)

    def display_mobiles(self):
        if len(self.mobiles) == 0:
            print("No mobiles available.")
        else:
            print("\nMobile List")
            print("-----------")
            for mobile in self.mobiles:
                mobile.display()


store = Store()

n = int(input("Enter number of mobiles: "))

for i in range(n):
    print("\nEnter details of Mobile", i + 1)
    brand = input("Brand: ")
    model = input("Model: ")
    price = float(input("Price: "))
    store.add_mobile(Mobile(brand, model, price))

store.display_mobiles()