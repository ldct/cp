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

### CODE HERE

def ok(K, a, b):
    # print("ok", K, a, b, ((a + b) // K) > (a//K + b//K))
    return ((a + b + 1) // K) > (a//K + b//K)

def ans(X, S):

    mut_S = list(S)

    leader = [-1]*len(S)
    count = defaultdict(int)

    cl = -1

    for i, s in enumerate(S):
        if s == '1':
            cl = -1
        elif s == '0':
            if cl == -1:
                cl = i
            leader[i] = cl

    for i, s in enumerate(S):
        if s == '0':
            count[leader[i]] += 1

    flips = 1

    for i in range(len(S)):
        if S[i:i+2] == "10" and count[leader[i+1]] == X-1 and flips > 0:
            flips -= 1
            mut_S[i] = '0'
        if S[i:i+2] == "01" and count[leader[i]] == X-1 and flips > 0:
            flips -= 1
            mut_S[i+1] = '0'
        if S[i:i+3] == "010" and ok(X, count[leader[i]], count[leader[i+2]]) and flips > 0:
            flips -= 1
            mut_S[i+1] = '0'


    leader = [-1]*len(S)
    count = defaultdict(int)

    cl = -1

    S = ''.join(mut_S)
    for i, s in enumerate(S):
        if s == '1':
            cl = -1
        elif s == '0':
            if cl == -1:
                cl = i
            leader[i] = cl

    ret = []

    for i, s in enumerate(S):
        if s == '0':
            count[leader[i]] += 1

    for l in range(len(S)):
        if leader[l] == l:
            ret += [count[l] // X]

    return sum(ret)

for _ in range(read_int()):
    N, X = read_int_tuple()
    S = input()
    print(ans(X, S))