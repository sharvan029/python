import csv

class Item:
    # pass
    pay_rate = 0.7
    all = []

    def __init__(self, name: str, price: int, quantity = 0):
        # print(f"Instance created for: {name}")
        # Run validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero"

        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        # self.price = self.price * Item.pay_rate
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))

            )

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

# print(Item.pay_rate)


Item.instantiate_from_csv()
print(Item.all)

#
# item1 = Item("Phone", 10000, 5)
# item2 = Item('Laptop', 40000, 2)
# item3 = Item('Mouse', 500, 3)
# item4 = Item('KeyBoard', 600, 3)
# item5 = Item('Headset', 1000, 2)

# print(item1)
# print(Item.all)
# print(item2.calculate_total_price())
# print(Item.all[0].name)

# for obj in Item.all:
#     print(obj.name)
