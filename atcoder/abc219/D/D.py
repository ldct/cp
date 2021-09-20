#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from functools import lru_cache

def make_fill(N, M, val):
    ret = []
    for _ in range(N):
        ret += [[val]*M]
    return ret

def dense_cache(func):
    N = 350
    cache = []
    for _ in range(N):
        cache += [make_fill(N, N, -1)]

    def memoized_func(i, j, k):
        if cache[i][j][k] != -1:
            return cache[i][j][k]
        result = func(i,j,k)
        cache[i][j][k] = result
        return result

    return memoized_func

INFINITY = 500
@lru_cache(None)
def ans(i, X, Y):
    if X <= 0 and Y <= 0: return 0
    if X < 0: X = 0
    if Y < 0: Y = 0
    if i == len(boxes): return INFINITY
    x, y = boxes[i]
    option1 = 1+ans(i+1, X-x, Y-y)
    option2 = ans(i+1, X, Y)

    r = min(option1, option2)
    if r >= INFINITY: return INFINITY
    return r

if False:
    N = read_int()
    X, Y = read_int_tuple()

    boxes = []
    for _ in range(N):
        boxes += [read_int_tuple()]

    r = ans(0, X, Y)
    if r > N: r = -1
    print(r)
else:
    import random
    N = 100
    boxes = [(random.randint(1, 20), random.randint(1, 20)) for _ in range(N)]
    print(ans(0, 300, 300))
