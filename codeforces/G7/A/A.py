#!/usr/bin/env python3

def ans(n):
    if n == 1:
        return -1
    if (n - 1) % 3 != 0:
        return "2"*(n-1) + "3"
    return "2"*(n-2) + "33"
T = int(input())

for _ in range(T):
    n = int(input())
    print(ans(n))