numbers = [1, 2, 3, 4]
# give new list by multiply by 2
out = []
for i in numbers:
    n = i*2
    out.append(n)

print(out)

out = [j*3 for j in numbers if j%2 ==0]
print(out)

out = [i + 10 for i in list(j*3 for j in numbers if j%2 ==0)]
print(out)