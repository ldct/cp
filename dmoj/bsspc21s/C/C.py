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

def maxProfit(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

N, K = read_int_tuple()
A = read_int_list()

groups = []

for _ in range(K):
    groups += [[]]

prefixes = [0]
for a in A:
    prefixes += [prefixes[-1] + a]

for i, p in enumerate(prefixes):
    groups[i % K] += [p]

print(max(map(maxProfit, groups)))
