#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify

### CODE HERE

def ans(K, A):
    ret = 0
    A = [-a for a in A]
    heapify(A)
    while len(A) >= K:
        ret += 1
        to_push = []
        for _ in range(K):
            to_push.append(heappop(A))
        to_push = [a + 1 for a in to_push]
        to_push = [a for a in to_push if a != 0]
        for a in to_push:
            heappush(A, a)
    return ret

N, K = read_int_tuple()
A = read_int_list()

print(ans(K, A))