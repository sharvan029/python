#[0,1,1,2,3,5,8,13..]

while True:
    n = int(input("type no of elements to be printed:"))
    l = [0,1]
    for i in range(n):
        if i >= 2:
            new = l[i-1] + l[i-2]
            l.append(new)
    print(l)
    print(','.join(str(x) for x in l))
    s = input("Do you want to exit(y/n)?")
    if s == 'y':
        break
