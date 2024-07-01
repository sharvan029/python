def check_prime(n):
    if n==2:
        print(str(n)  + " is a prime number")
    for i in range(2, n):
        if n%i ==0:
            print(str(n) +" divisible by " + str(i) + " ,not a prime number")
            break
        else:
            if i == n-1:
                print(str(n)  + " is a prime number")
            i+=1

check_prime(9)