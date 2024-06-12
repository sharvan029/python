# from typing import List
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # create all combinations
    temp_list = []
    out = []
    # take i item from x
    out = list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n)
                

    print(out)



    # filter i+j+k != n