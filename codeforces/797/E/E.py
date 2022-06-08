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

def ans(K, A):
    vals = [a % K for a in A]
    cv = Counter(vals)

    cost = 0
    num_matched = 0

    while num_matched != len(A):
        for v in cv:
            w = (K - v) % K
            if w == v and cv[v] >= 2:
                f = (cv[v] // 2)
                num_matched += 2*f
                cv[v] -= 2*f
                # cost += 0
            else:
                for _t in range(w, w + K):
                    t = (_t % K)
                    if cv[t] > 0:
                        # match v, t

                        if t == v:
                            f = cv[v] // 2
                            num_matched += 2*f
                            cv[v] -= 2*f
                            cost += f*((v+v) % K)
                        else:
                            f = min(cv[t], cv[v])
                            cost += f*((t + v) % K)
                            cv[v] -= f
                            cv[t] -= f
                            num_matched += 2*f
    return (sum(A) - cost) // K
    return K, vals, cost

for _ in range(read_int()):
    N, K = read_int_tuple()
    A = read_int_list()
    print(ans(K, A))