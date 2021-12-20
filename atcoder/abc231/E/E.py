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

def greedy_10(X):
    return sum(map(int, str(X)))

def ans_10(N):
    ret = greedy_10(N)
    for Y in range(N, 2*N+10):
        ret = min(ret, greedy_10(Y) + greedy_10(Y-N))
    return ret

def greedy_10_lst(X):
    return list(map(int, str(X)))

def ans_10_fast(X):
    ret = list(map(int, greedy_10_lst(X)[::-1])) + [0]
    for i in range(len(ret)):
        if (10-ret[i] < ret[i]) or ((10-ret[i] == ret[i]) and ret[i+1] >= 5):
            ret[i] = ret[i]-10
            ret[i+1] += 1
    return sum(map(abs,ret))

def greedy(X, coins):
    ret = 0
    for c in coins:
        ret += X // c
        X %= c
    return ret

def ans(X, coins):
    coins = sorted(coins)[::-1]
    ret = greedy(X, coins)
    def score(Y):
        return greedy(Y, coins) + greedy(Y-X, coins)

    for Y in range(X, 2*X+10):
        ret = min(ret, score(Y))

    for Y in range(X, 2*X+10):
        if ret == score(Y):
            print(Y)

    return ret

def greedy_lst(X, coins):
    coins = sorted(coins)[::-1]
    ret = []
    for c in coins:
        ret += [X // c]
        X %= c
    return ret

def ans_fast(X, coins):
    ret = greedy_lst(X, coins)[::-1]
    coins = sorted(coins)

    ratios = [None]*(len(coins)-1)
    for i in range(len(coins)-1):
        ratios[i] = coins[i+1] // coins[i]

    ratios += [float("inf")]

    for i in range(len(ret)):
        if (ret[i] > ratios[i] / 2):
            ret[i] = ret[i]-ratios[i]
            ret[i+1] += 1
    return sum(map(abs,ret))

if True:
    print(ans_fast(49, [1,2,14]))
    print(ans(49, [1,2,14]))
elif True:
    for X in range(2, 2000):
        assert(ans_10_fast(X) == ans(X, [1000, 100, 10, 1]))
        assert (ans_10_fast(X) == ans_10(X))
else:
    _, X = read_int_tuple()
    coins = read_int_list()
    print(ans(X, coins))