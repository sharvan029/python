from item import Item
from phone import Item

# Item.instantiate_from_csv()
# print(Item.all)

item1 = Item('MyItem', 750)
item1.send_email()

# we are able to change the value of an attribute many times
# item1.name = 'OtherItem'

