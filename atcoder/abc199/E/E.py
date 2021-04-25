#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from functools import lru_cache

def popcount(x):
    return bin(x).count('1')

### CODE HERE

N, M = read_int_tuple()
constraints = []
for _ in range(M):
    constraints += [read_int_tuple()]

@lru_cache(None)
def good(mask):
    subset = []

    for i in range(N):
        if mask & (1 << i):
            subset += [i+1]

    for x, y, z in constraints:
        if x == len(subset):
            if len([e for e in subset if e <= y]) > z:
                return False
    return True

@lru_cache(None)
def ans(mask):
    if popcount(mask) == 0: return 1
    if not good(mask): return 0

    ret = 0
    for i in range(N):
        if 0 == mask & (1 << i): continue
        ns = mask & ~(1 << i)
        ret += ans(ns)

    return ret

print(ans((1 << (N)) - 1))