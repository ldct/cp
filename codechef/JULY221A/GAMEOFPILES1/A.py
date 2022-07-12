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

# tag:game theory

class PileGame:
    def next_states(self, state):
        if 1 in state:
            return 0 # win for current player
        ret = []
        for i in range(len(state)):
            next_state = list(state)
            next_state[i] -= 1
            ret += [tuple(sorted(next_state))]
        return ret

g = PileGame()
print(g.next_states([1, 2, 3, 4, 5]))


# def ans(A):
#     if 1 in A:
#         return "CHEF"
#     r = sum(A) - 2*len(A)
#     if r % 2 == 0:
#         return "CHEFINA"
#     return "CHEF"

# for _ in range(read_int()):
#     input()
#     print(ans(read_int_list()))