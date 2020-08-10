#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

N, Q = input().split()
Q = int(Q)
A = list(map(int, input().split()))[::-1]

B = []
l = A[0]
u = A[0]

for a in A:
    l = min(l, a)
    u = max(u, a)
    B += [(l, u)]

del l
del u

def ok(i, l, u):
    ll, uu = B[i]
    return l <= ll <= uu <= u

def ans(l, u):
    low = 0
    high = len(B)-1

    if ok(high, l, u):
        return len(B)

    if not ok(low, l, u):
        return 0


    while high - low >= 2:
        # assert(ok(low, l, u))
        # assert(not ok(high, l, u))

        mid = (high + low) // 2
        if ok(mid, l, u):
            low = mid
        else:
            high = mid

    for i in range(low, len(B)):
        if ok(i, l, u):
            continue
        return i
    return len(B)

for _ in range(Q):
    L, e = input().split()
    L = int(L)
    e = int(e)
    l = L-e
    u = L+e

    print(ans(l, u))