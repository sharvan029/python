n=153
strn = str(n)
res = 0
for x in strn:
    res = res + int(x)**3
if res == n:
    print(str(n) + ' is armstrong')
else:
    print('{n} is not armstrong')