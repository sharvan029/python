class Item:
    # pass
    def __init__(self, name, price, quantity):
        # print(f"Instance created for: {name}")
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Phone", 10000, 5)
# item1.Name = 'Phone'
# item1.price = 10000
# item1.quantity = 2

print(item1.name)
print(item1.price)
print(item1.quantity)
print(item1.calculate_total_price())
# print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item('Laptop', 40000, 2)
# item2.Name = 'Laptop'
# item2.price = 40000
# item2.quantity = 1
print(item2.name)
print(item2.price)
print(item2.quantity)
print(item2.calculate_total_price())

# print(item1.calculate_total_price(item2.price, item2.quantity))

# item1.total_price =
# print(type(item1.Name))
# print(type(item1.price))
# print(type(item1.quantity))