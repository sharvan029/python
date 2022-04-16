import csv as csv
from item import Item


class Phone(Item):

    def __init__(self, name: str, price: int, quantity=0, broken_phones=0):
        # Call to super functions to have access to all attributes/methods
        super().__init__(
            name, price, quantity
        )

        # Run validation to the received arguments
        assert broken_phones >= 0, f"broken_phones {broken_phones} is not greater than  or equal to  zero"

        # assign to self object
        self.broken_phones = broken_phones






