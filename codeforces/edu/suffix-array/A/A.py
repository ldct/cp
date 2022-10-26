#!/usr/bin/env python3

import io, os, sys
from sys import stdin, stdout

# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

### CODE HERE

def argsort(S):
    pairs = [(a, i) for (i, a) in enumerate(S)]
    pairs.sort()
    return pairs

def lookup_of(P, C):
    ret = []
    for p, c in zip(P, C):
        ret += [(p, c)]
    ret.sort()
    return [e[-1] for e in ret]

def compress(A):
    C = []
    last_a = None
    last_c = -1
    for a in A:
        if a != last_a:
            last_c += 1
        C += [last_c]
        last_a = a
    return C

def suffix_array(S):
    assert("$" not in S)
    S += "$"
    N = len(S)

    # K = 0
    SP = argsort(S)
    C = compress([e[0] for e in SP])
    P = [e[-1] for e in SP]
    L = lookup_of(P, C)

    K = 1
    while True:
        substrings = [(L[i%N], L[(i+K)%N]) for i in range(N)]
        SP = argsort(substrings)
        C = compress([e[0] for e in SP])
        P = [e[-1] for e in SP]
        L = lookup_of(P, C)

        if len(C) == C[-1] + 1:
            break
        else:
            K *= 2

    # print("K=", K)
    return P

if True:
    print(*suffix_array(input()))
else:
    import random
    N = 10**5
    tc = ''.join(random.choice("a") for _ in range(N))
    suffix_array(tc)
    # print(tc, suffix_array(tc))