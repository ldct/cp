#!/usr/bin/env pypy3

N, K = input().split(' ')
K = int(K)
A = input().split(' ')
A = [int(a) for a in A if len(a)]

from functools import lru_cache

@lru_cache(None)
def f(x):
    ret = 0
    for a in A:
        ret += abs(x-a)**K
    return -ret

l = 0
r = 5*10**4

for _ in range(500):
    m1 = l + (r-l)//3
    m2 = r - (r-l)//3

    if f(m1) < f(m2):
        l = m1
    else:
        r = m2

max_val = max(f(i) for i in range(l-1, r+2))

i = r+3

import sys

while True:
    if f(i) == max_val and f(i-1) < max_val:
        print(i)
        sys.exit(0)
    i -= 1