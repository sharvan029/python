def myf(n):
    return lambda a: a*n

b = myf(2) # f(n) : return 2n
print(b(10))


c = myf(3) #f(n): return 3n
print(c(2))