#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

if True:
    import random
    N = 50
    X = 10**17
    A = [random.randint(1, 10**7) for _ in range(N)]
    print(N, X)
    print(*A)
    import sys
    sys.exit(0)
else:
    N, X = read_int_tuple()
    A = read_int_list()

from functools import lru_cache

@lru_cache(None)
def mc(i, target, M, c):
    # the sum of the subset of A[i:] with maximum sum whose sum is == target modulo

    if c < 0: return -1

    def rm(x):
        return ((x % M) + M) % M

    if i == len(A):
        if target == 0 and c == 0: return 0
        return -1

    option1 = mc(i+1, target, M, c)
    option2 = mc(i+1, rm(target - A[i]), M, c-1)

    ret = set()
    if option1 != -1: ret.add(option1)
    if option2 != -1: ret.add(option2 + A[i])

    if len(ret) == 0: return -1

    return max(ret)

best = float("inf")

for t in range(1, N+1):
    s = mc(0, X % t, t, t)
    print(s)
    if s == -1: continue
    assert((X - s) % t == 0)
    best = min(best, (X - s) // t)

print(best)