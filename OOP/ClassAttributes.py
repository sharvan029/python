class Item:
    # pass
    pay_rate = 0.7
    def __init__(self, name: str, price: int, quantity = 0):
        # print(f"Instance created for: {name}")
        # Run validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero"

        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        # self.price = self.price * Item.pay_rate
        self.price = self.price * self.pay_rate

print(Item.pay_rate)
item1 = Item("Phone", 10000, 5)
item1.apply_discount()
print(item1.calculate_total_price())
# print(Item.__dict__)

# print(item1.__dict__)
# print(item1.pay_rate)
# print(item1.calculate_total_price())

item2 = Item('Laptop', 40000, 2)
item2.pay_rate = 0.5
item2.apply_discount()
print(item2.calculate_total_price())


# print(item2.calculate_total_price())
