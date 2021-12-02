#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(H, A):
    A += [float("inf")]
    gaps = []
    for i in range(len(A) - 1):
        gaps += [A[i+1] - A[i]]
    def damage(K):
        return sum([min(K, g) for g in gaps])
    def ok(K):
        return damage(K) >= H

    low = 0
    high = H

    assert(not ok(low))
    assert(ok(high))

    while high - low > 2:
        mid = (low + high) // 2
        if ok(mid):
            high = mid
        else:
            low = mid

    for i in range(low, low+10):
        if ok(i): return i

    return H, gaps

for _ in range(read_int()):
    N, H = read_int_tuple()
    A = read_int_list()
    print(ans(H, A))