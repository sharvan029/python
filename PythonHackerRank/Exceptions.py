# # try:
# #     # taking inputs a and b
# #     a, b = map(int, input().split())
# #     div = a//b
# #     print(div)
# # except Exception as e:
# #     print("Error Code:", e)
#
# #Checking value error exception
#
# # while True:
# #     try:
# #         x = int(input("Please enter a number: "))
# #         break
# #     except ValueError:
# #         print("Oops!  That was no valid number.  Try again...")
#
# #using raise
# a = 5
#
# if a % 2 != 0:
# 	raise Exception("The number shouldn't be an odd integer")
#
# s = 'apple'
#
# try:
#     num = int(s)
# except ValueError:
#     raise ValueError("String can't be changed into integer")

#exception with out Exception class


# s = 'apple'
#
# try:
#     num = int(s)
# except:
#     raise

import re

def validateregex(reg):
    try:
        val = re.compile(reg)
    except re.error:
        return False
    return True

n = int(input("no of test cases: "))
for i in range(n):
    s = input("Type regex")
    print(validateregex(s))



