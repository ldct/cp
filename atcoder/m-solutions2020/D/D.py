#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

input()
A = input().split(' ')
A = list(map(int, A))

yen = 1000
stocks = 0

for i in range(len(A)):
    if i < len(A)-1 and A[i+1] > A[i]:
        # buy
        new_stocks = yen // A[i]
        stocks += new_stocks
        yen -= new_stocks*A[i]
    if i == len(A)-1 or A[i+1] < A[i]:
        # sell
        yen += stocks*A[i]
        stocks = 0

print(yen)