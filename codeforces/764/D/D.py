#!/usr/bin/env pypy3

from sys import stdin, stdout

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

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

### CODE HERE

def ok(K, num_pairs, num_odds, sz):
    need = [sz]*K

    for i in range(K):
        pairs_to_kill = min(need[i] // 2, num_pairs)

        need[i] -= 2*pairs_to_kill
        num_pairs -= pairs_to_kill

        if need[i] > 1: return False

    return sum(need) <= num_odds + 2*num_pairs

def ans(K, S):

    cS = Counter(S)

    num_pairs = 0
    num_odds = 0

    for a in ALPHABET:
        f = cS[a]
        num_pairs += (f // 2)
        num_odds += (f % 2)

    low = 1
    high = len(S)+1

    assert(ok(K, num_pairs, num_odds, low))
    assert(not ok(K, num_pairs, num_odds, high))

    while high - low > 2:
        mid = (low + high) // 2
        if ok(K, num_pairs, num_odds, mid):
            low = mid
        else:
            high = mid

    for ret in range(low, low+10):
        if not ok(K, num_pairs, num_odds, ret):
            return ret - 1

    assert(False)



if False:
    print(ok(3, "aaaaaa", 1))
else:
    for _ in range(read_int()):
        N, K = read_int_tuple()
        S = input()
        print(ans(K, S))