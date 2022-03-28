#!/bin/python


# This script capitalises the given String
def solve(s):
    list = s.split()
    #print(list)
    nstring = ''
    for x in list:
        nstring = nstring + x.capitalize() +' '
    return nstring

if __name__ == '__main__':

    s = '12hi iam tony'
    result = solve(s)
    print(result)

