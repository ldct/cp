#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

import bisect

def ans(sA, A, x, y):
    key = x+y
    if key in sA:
        return -1
    return bisect.bisect_left(A,x+y)
    
T = int(input())

for _ in range(T):
    input()
    A = input().split(' ')
    A = list(map(int, A))
    A = sorted(A)
    sA = set(A)
    Q = int(input())
    for _ in range(Q):
        x, y = input().split(' ')
        x = int(x)
        y = int(y)
        print(ans(sA, A, x, y))
