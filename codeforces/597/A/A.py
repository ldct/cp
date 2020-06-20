#!/usr/bin/env python3

import math

def ans(a, b):
    if math.gcd(a, b) == 1:
        return "finite"
    else:
        return "infinite"

T = int(input())

for _ in range(T):
    a, b = input().split(' ')
    a = int(a)
    b = int(b)
    print(ans(a, b))