#!/usr/bin/env python3

T = int(input())

def ans(n, m):
    if n == 1:
        return 0
    if n == 2:
        return m
    else:
        return 2*m

for t in range(T):
    n, m = input().split(' ')
    n = int(n)
    m = int(m)
    print(ans(n, m))