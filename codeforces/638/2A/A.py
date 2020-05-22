#!/usr/bin/env python3

T = int(input())

def ans():
    n = int(input())

    total = 2**(n+1) - 2

    a = 2**n + 2**(n // 2) - 2
    b = total - a

    return a - b

for t in range(T):
    print(ans())