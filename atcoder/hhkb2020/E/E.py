#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from functools import lru_cache

def dense_cache(func):
    cache = []
    for _ in range(H+10):
        cache += [[-1]*(W+10)]

    def memoized_func(i, j):
        if cache[i+5][j+5] != -1:
            return cache[i+5][j+5]
        result = func(i,j)
        cache[i+5][j+5] = result
        return result

    return memoized_func

### CODE HERE

MODULUS = 10**9+7

def ans(H, W, S):

    i_min = []
    for _ in range(H): i_min += [[-1]*(W)]

    for j in range(W):
        if S[0][j] == '#':
            i_min[0][j] = 0
        else:
            i_min[0][j] = -1
        for i in range(1,H):
            if S[i][j] == '#':
                i_min[i][j] = i
            else:
                i_min[i][j] = i_min[i-1][j]

    i_max = []
    for _ in range(H): i_max += [[-1]*(W)]

    for j in range(W):
        if S[H-1][j] == '#':
            i_max[H-1][j] = H-1
        else:
            i_max[H-1][j] = H
        for i in range(H-2,-1,-1):
            if S[i][j] == '#':
                i_max[i][j] = i
            else:
                i_max[i][j] = i_max[i+1][j]

    j_min = []
    for _ in range(H): j_min += [[-1]*(W)]

    for i in range(H):
        if S[i][0] == '#':
            j_min[i][0] = 0
        else:
            j_min[i][0] = -1
        for j in range(1,W):
            if S[i][j] == '#':
                j_min[i][j] = j
            else:
                j_min[i][j] = j_min[i][j-1]

    j_max = []
    for _ in range(H): j_max += [[-1]*(W)]

    for i in range(H):
        if S[i][W-1] == '#':
            j_max[i][W-1] = W-1
        else:
            j_max[i][W-1] = W
        for j in range(W-2,-1,-1):
            if S[i][j] == '#':
                j_max[i][j] = j
            else:
                j_max[i][j] = j_max[i][j+1]

    def visible(I, J):
        # print(i_min, i_max, j_min, j_max)
        r = (i_max[i][j] - i_min[i][j] - 1) + (j_max[i][j] - j_min[i][j] - 1) - 1
        return r


    num_tidy = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                num_tidy += 1

    @lru_cache(None)
    def fastpow(t):
        return pow(2, t, MODULUS)

    ret = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                v = visible(i, j)
                ret += fastpow(num_tidy) - fastpow(num_tidy - v)
                ret %= MODULUS

    ret += MODULUS
    ret %= MODULUS

    return ret

if True:
    S = []
    H, W = read_int_tuple()
    for _ in range(H):
        S += [input()]
else:
    import random
    H, W = 2000,2000
    S = []
    for _ in range(H):
        S += [''.join(random.choice('.') for _ in range(W))]
print(ans(H, W, S))
