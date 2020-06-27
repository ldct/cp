#!/usr/bin/env pypy3

from collections import Counter
import math

def lcm(a, b):
    return a*b // math.gcd(a,b)

def all_lcm(arr):
    ret = arr[0]
    for a in arr:
        ret = lcm(ret, a)
    return ret

def ans(D):
    freqs = Counter(D)

    doubles = []

    for f in freqs:
        if freqs[f] >= 2:
            doubles += [f]

    G = max(doubles)
    L = all_lcm(D)
    
    B = max(D)

    A = G*L // B

    return (A, B)

input()
D = input().split(' ')
D = list(map(int, D))
print(*ans(D))