#search
import re

result = re.search(r'\d+', 'The house number is 1234')
print(result.group())

# match

result = re.match(r'Hello', 'Hello World')
print(result.group())

# find all

r3 = re.findall(r'\d+', '123 ABC 456 DEF 789')
print(r3)

string = 'a20b30c40'
r4 = re.findall(r'\d+', string)
print(r4)
s = 0
for x in r4:
    s += int(x)
print(s)

# substitute
r5 = re.sub('\s+', '-',  'This is a test')
print(r5)



#email validation

pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
email = 'sharven9499244@example.com'

result = re.match(pattern, email)

if result:
    print('valid email')
else:
    print('Not valid email')


# extract date

inp = 'Today\'s date is 26-06-2024. Tomorrow will be 27-06-2024.'

pattern = r'\d{2}-\d{2}-\d{4}'

r6 = re.findall(pattern, inp)
print(r6)

# replace pattern



inp = 'The color is red. The color is blue.'
pattern = 'red|blue'

r7 = re.sub(pattern, 'green', inp)
print(r7)