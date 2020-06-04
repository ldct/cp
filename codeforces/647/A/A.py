#!/usr/bin/env python3

T = int(input())

def ans(a, b):
    if b < a: return ans(b, a)
    if a == b: 
        return 0
    if 8*a <= b:
        return 1 + ans(8*a, b)
    if 4*a <= b:
        return 1 + ans(4*a, b)
    if 2*a <= b:
        return 1 + ans(2*a, b)
    return float("inf")

for t in range(T):
    a, b = input().split(' ')
    a = int(a)
    b = int(b)

    r = ans(a, b)
    if r == float("inf"):
        print(-1)
    else:
        print(r)
