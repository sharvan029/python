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
        self.__name = name # double underscore is used to make it private
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise Exception("Price should be greater than zero")
        else:
            self.__price = value

    def apply_discount(self):
        # self.price = self.price * Item.pay_rate
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_rate=0.05):
        self.__price = self.__price + self.__price * increment_rate

    @property
    # Property decorator = Read only attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value)> 10:
            raise Exception("The name is too long")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity



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

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

    @property
    def read_only_name(self):
        return "ron"

    def __connect(self, smtp_server):
        pass

    def __prepare_body(self):
        return f"""Hi there, we have {self.name} of quantity {self.quantity}" 
               regards,
               Hameed"""

    def __send(self):
        pass

    def send_email(self):
        self.__connect()
        self.__prepare_body()
        self.__send()





