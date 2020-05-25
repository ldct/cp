#!/usr/bin/env python3
import math

T = int(input())

def ans(n, k):
    for f in range(1, math.ceil(math.sqrt(n))):
        if n % f > 0: continue
        cf = n // f
        if cf <= k: return f
    for f in range(math.ceil(math.sqrt(n)), 0, -1):
        if n % f > 0: continue
        if f <= k: return n // f

    return '?'

for t in range(T):
    n, k = input().split(' ')
    n, k = int(n), int(k)
    print(ans(n, k))