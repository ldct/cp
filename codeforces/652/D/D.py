#!/usr/bin/env pypy3

import array

MODULUS = 10**9+7

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

memoT = array.array('i', [-1]*(2*10**6+1))
memoF = array.array('i', [-1]*(2*10**6+1))

def ans(i, disallow_occupy):
    if i <= 2: return 0
    if i == 3: 
        if disallow_occupy: return 0
        return 4
    if i == 4:
        return 4

    if disallow_occupy and memoT[i] != -1: return memoT[i]
    if not disallow_occupy and memoF[i] != -1: return memoF[i]

    choice1 = 2*ans(i-2, True) + ans(i-1, True) + 4 
    choice1 = choice1 % MODULUS
    if disallow_occupy: choice1 = float("-inf")

    choice2 = 2*ans(i-2, False) + ans(i-1, False)
    choice2 = choice2 % MODULUS

    if disallow_occupy:
        memoT[i] = max(choice1, choice2)
        return memoT[i]
    else:
        memoF[i] = max(choice1, choice2)
        return memoF[i]    

for i in range(5, 100):
    print(f"{i} {ans(i, True)} {ans(i, False)}")
