#!/usr/bin/env python3
import math

T = int(input())

def possible(n, m, a, b):
    if not (n*a == m*b):
        return False

    ans = []
    for i in range(n):
        ans += [['0']*m]

    for t in range(n):
        x0 = t
        y0 = (t*a) % m

        for y in range(a):
            ans[x0][(y0+y) % m] = '1'

    return ans

def ans(n, m, a, b):
    x = possible(n, m, a, b)
    if x:
        print("YES")
        for row in x:
            print(''.join(row))
        return
    print("NO")

for t in range(T):
    n, m, a, b = input().split(' ')
    n, m, a, b = int(n), int(m), int(a), int(b)

    ans(n, m, a, b)
