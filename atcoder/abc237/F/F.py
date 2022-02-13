#!/usr/bin/env pypy3

import io, os
from sys import stdin, stdout

# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache
from copy import deepcopy

### CODE HERE

MODULUS = 998244353

def next_state(state, p):

    if state is None: return None
    x, y, z = state

    next_x = min(x, p)

    next_y = y
    if p > x:
        next_y = min(y, p)

    next_z = z
    if p > y:
        next_z = min(z, p)

    if p > z: return None

    return (next_x, next_y, next_z)

def lis_of_state(state):
    if state == None: return 4
    x, y, z = state
    if z != float("inf"): return 3
    if y != float("inf"): return 2
    return 1

def ans(N, M):
    dp = []
    for _ in range(N+1):
        dp += [defaultdict(int)]

    dp[0][(float("inf"), float("inf"), float("inf"))] = 1

    for i in range(N):
        for k in dp[i]:
            for p in range(1, M+1):
                ns = next_state(k, p)
                if ns is not None:
                    dp[i+1][ns] += dp[i][k]
                    dp[i+1][ns] %= MODULUS


    ret = 0
    for k in dp[-1]:
        if lis_of_state(k) == 3:
            ret += dp[-1][k]

    return ret % MODULUS

def state_of_arr(arr):
    state = (float("inf"), float("inf"), float("inf"))
    for p in arr:
        state = next_state(state, p)
    return state

def lis_of_arr(arr):
    return lis_of_state(state_of_arr(arr))

print(ans(*read_int_tuple()))
