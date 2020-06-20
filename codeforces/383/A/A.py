#!/usr/bin/env python3

def ans(n):
    if n == 0: return 1
    return [6, 8, 4, 2][n % 4]

n = int(input())
print(ans(n))
