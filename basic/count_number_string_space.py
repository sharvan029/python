string = 'Hello World, Keep Going1,2,3... infinite times'

import re

digitCount = re.findall(r'\d+', string)
print(len(digitCount))

spaceCount = re.findall(' ', string)
print(len(spaceCount))

charCount = re.findall(r'[a-zA-Z]', string)
print(len(charCount))



#  Counting Special Characters in a String

print(' Counting Special Characters in a String')

string2 = 'Hello World!, Keep Going1,2,3... infinite times :)'

r8 = re.sub(r'[\w]', '', string2)
print(len(r8))

r9 = re.findall(r'[\w]', string2)
print(r9)

# replace white space

string = "C O D E"
# spaces = re.compile(r'\s+')
result = re.sub(r'\s+', '', string)
print(result)