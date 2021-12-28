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
from bisect import bisect_left

### CODE HERE

def ans_slow(S):
    ret = 0
    for i in range(len(S)):
        ret += int(S[:i+1])
    return ret

def ans(S):
    ret = 0
    N = len(S)
    e = N
    for i in range(N):
        x = int(S[i])
        ret += x*(10**e-1)
        e -= 1
    return ret // 9

def ans_fast(S):
    X = int(S)
    total = sum(map(int, S))
    return (10*X - total) // 9

print(ans_fast(input()))
