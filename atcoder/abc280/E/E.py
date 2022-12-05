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
from fractions import Fraction

def egcd(a, b):
    """
    returns
    gcd(a, b), s, r
    s.t.
    a * s + b * r == gcd(a, b)
    """
    s, old_s = 0, 1
    r, old_r = b, a
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    return old_r, old_s, (old_r - old_s * a) // b if b else 0

def modinv(a, m):
    """returns the modular inverse of a w.r.t. to m, works when a and m are coprime"""
    g, x, _ = egcd(a % m, m)
    return x % m if g == 1 else None

### CODE HERE

N, P = read_int_tuple()

def ans_frac(N, P):
    p2 = Fraction(P, 100)
    p1 = 1-p2

    def ans(S):
        if S <= 0:
            return 0
        return p2*(1 + ans(S-2)) + p1*(1 + ans(S-1))
    return ans(N)

MODULUS = 998244353

def ans_mod(N, P):
    p2 = P * modinv(100, MODULUS)
    p2 %= MODULUS
    p2 += MODULUS
    p2 %= MODULUS

    p1 = 1 - p2
    p1 %= MODULUS
    p1 += MODULUS
    p1 %= MODULUS

    @lru_cache(None)
    def ans(S):
        if S <= 0:
            return 0
        return (p2*(1 + ans(S-2)) + p1*(1 + ans(S-1))) % MODULUS
    return ans(N)

print(ans_mod(N, P))