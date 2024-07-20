n = int(input("please enter number: "))
temp = 0
if n >2:
    for i in range(2, n//2):
        if n%i == 0:
            temp =1
            break
if temp == 0:
    print(str(n) + ' is a prime number')
else:
    print(str(n) + ' is not a prime number')