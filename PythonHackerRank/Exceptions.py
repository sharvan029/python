try:
    # taking inputs a and b
    a, b = map(int, input().split())
    div = a//b
    print(div)
except Exception as e:
    print("Error Code:", e)

