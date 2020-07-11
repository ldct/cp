#!/usr/bin/env pypy3

from math import sqrt
def count(k, t):
    if k*k - 4*t < 0: return 0
    if t == 0: return 0

    r = (-k + sqrt(k*k - 4*t)) / 2
    r = int(r)

    if r*r + k*r + t == 0 and 1 <= r: return 1
    return 0

def f(N):
    ret = 0
    for x in range(1, N+1):
        for y in range(1, N+1):
            k = x+y
            t = x*x + y*y + x*y - N
            # count solutions to z^2 + kz + t = 0
            ret += count(k, t)
    return ret


ans = dict()

for i in range(1, 10**4+1):
    ans[i] = 0

for x in range(1, 10**2+1):
    for y in range(1, 10**2+1):
        if (x**2 + y**2 > 10**4): continue
        for z in range(1, 10**2+1):
            n = x*x + y*y + z*z + x*y + x*z + y*z
            if n > 10**4: continue
            ans[n] += 1

N = int(input())
for i in range(1, N+1):
    print(ans[i])