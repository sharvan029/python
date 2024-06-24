
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a//b
    print(c)
except ZeroDivisionError:
    raise Exception("Zero Division Error")
finally:
    print("Execution completed")