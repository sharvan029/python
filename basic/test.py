name = 'Hameed Sharvan'
print(name.swapcase())


# function as argument
def shout(x):
    return x.upper()
def whisper(x):
    return x.lower()

def hofunction(func):
    print(func("Hello This is an example for Function as argument"))

hofunction(shout)
hofunction(whisper)

# convert integer to decimal
import decimal
number = 1000
dnum = decimal.Decimal(number)
print(dnum)
print(type(dnum))

# reversing a string

string = "Hello World, Trust in Process"

rev_str = string[::-1]
print(rev_str)
print(rev_str.swapcase())

##reverse posistion and swap case

lst_str = string.split(' ')
# rev_lst_str = lst_str[::-1]
rev_lst_str = list(reversed(lst_str))
nlst = [x.swapcase() for x in rev_lst_str]
ostr = ''
for x in nlst:
    ostr +=x + ' '
print(ostr)

# Count vowels in word
vowels = ['a', 'e', 'i', 'o', 'u']

cnt = 0
lst = list(string)

d =  dict()
for x in lst:
    if x in d.keys():
        d[x] = d[x] + 1
    else:
        d[x] = 1
print(d)
for v in vowels:
    if v in d.keys():
        # print(v)
        # cnt = cnt + d[v]
        pass
print(cnt)     

# alternate

for x in string:
    if x in vowels:
        cnt += 1
print(cnt)

# count consonents

ccnt = 0
for x in string:
    if x not in vowels:
        ccnt += 1
print(len(string))
print(ccnt)




