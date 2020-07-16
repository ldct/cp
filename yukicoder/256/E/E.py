#!/usr/bin/env python3

MODULUS = 10**9+7

from collections import defaultdict

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

N, M, K = input().split(' ')
N = int(N)
M = int(M)
K = int(K)

from functools import lru_cache

def ans(length, last, target):
    # how many length-`length` progressions are there with last chord `last` and complexity `target`
    if length == 1:
        if target == 0: return 1
        return 0
    if target < 0: return 0

    ret = 0
    for (prev, cost) in neighbours[last]:
        ret += ans(length-1, prev, target-cost)
        ret = ret % MODULUS
    return ret

neighbours = defaultdict(set)

for _ in range(M):
    P, Q, C = input().split(' ')
    P = int(P)
    Q = int(Q)
    C = int(C)

    neighbours[Q].add((P, C))

ret = sum(ans(N, v, K) for v in range(1, 301))
print(ret % MODULUS)
