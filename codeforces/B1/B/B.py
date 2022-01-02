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

### CODE HERE

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"

def no_digits(S):
    for c in DIGITS:
        if c in S: return False
    return True

def int_of(S):
    ret = 0
    for c in S:
        ret *= 26
        ret += (ord(c) - ord('A') + 1)
    return ret

def c1(S):
    old_S = S
    S = S.rstrip(DIGITS)
    if no_digits(S):
        left = old_S.strip(ALPHABET)
        return f"R{left}C{int_of(S)}"
    return None

def cdiv(x, y):
    return x // y if x % y == 0 else x // y + 1

def alpha_of(x):
    x = int(x)
    ret = []
    while x > 0:
        q = cdiv(x, 26) - 1
        ret += [x - q*26]
        x = q
    ret = ret[::-1]
    return ''.join(chr(ord('A') + c - 1)for c in ret)

def c2(S):
    S = S[1:]
    r, c = S.split('C')
    return alpha_of(c) + r

def ans(S):
    r = c1(S)
    if r is not None: return r
    return c2(S)

for _ in range(read_int()):
    print(ans(input()))