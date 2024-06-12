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
    for i in range(x+1):
        # take j from y
        for j in range(y+1):
            # take k from z
            for k in range(z+1):
                # check if i+j+k !=n
                if i+j+k != n:
                    temp_list = [i, j, k]
                    # append list with i,j,k
                    out.append(temp_list)
    print(out)



    # filter i+j+k != n