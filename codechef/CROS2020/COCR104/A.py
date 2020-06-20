#!/usr/bin/env python3

import math

def ans3(a, b, L, R):
    next_a = True
    ret = 0
    pos = 0

    while True:
        if next_a:
            pos += a
            next_a = False
        else:
            pos += b
            next_a = True
        
        if L <= pos <= R: ret += 1
        if pos > R: return ret

def ans2(a, b, L, R):
    next_a = True
    ret = 0
    pos = (L // (a + b) - 1) * (a + b)

    while True:
        if next_a:
            pos += a
            next_a = False
        else:
            pos += b
            next_a = True
        
        if L <= pos <= R: ret += 1
        if pos > R: return ret

def ans(a, b, L, R):
    l = math.ceil(L / (a+b))
    r = math.floor(R / (a+b))

    if l == 0: l += 1

    ll = l*(a+b) - b
    rr = r*(a+b) + a

    if l > r:
        if ll == rr:
            if L <= ll <= R: return 1
            return 0
        else:
            ret = 0
            if L <= ll <= R: ret += 1
            if L <= rr <= R: ret += 1
            return ret

    ret = 0

    if L <= ll <= R: ret += 1
    if L <= rr <= R: ret += 1

    if (r - l + 1)*2 - 1 > 0:
        ret += (r - l + 1)*2 - 1

    return ret

# for _ in range(10000):
#     import random
#     a = random.randint(1, 5)
#     b = random.randint(1, 5)
#     L = random.randint(1, 100)
#     R = random.randint(1, 100)

#     if ans(a, b, L, R) is not None and ans(a, b, L, R) != ans3(a, b, L, R):
#         print(a, b, L, R, ans3(a, b, L, R))


T = int(input())

for _ in range(T):
    [a, b, L, R, *rest] = input().split(' ')
    a = int(a)
    b = int(b)
    L = int(L)
    R = int(R)
    print(ans(a, b, L, R))