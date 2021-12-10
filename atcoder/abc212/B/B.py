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

def ans(S):
    if len(set(S)) == 1: return "Weak"
    new_S = [(S[0] + i) % 10 for i in range(4)]
    if S == new_S: return "Weak"
    return "Strong"

S = list(map(int, input()))
print(ans(S))