from item import Item
from phone import Item

# Item.instantiate_from_csv()
# print(Item.all)

item1 = Item('MyItem', 750)
print(item1.read_only_name)
item1.name = 'newname1111111111111111'
print(item1.name)
# print(item1.__name)

# we are able to change the value of an attribute many times
# item1.name = 'OtherItem'

