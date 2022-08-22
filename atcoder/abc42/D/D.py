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

MODULUS = 10**9 + 7

def make_nCr_mod(max_n=5 * 10**5 + 100, mod=10**9 + 7):
    fact, inv_fact = [0] * (max_n + 1), [0] * (max_n + 1)
    fact[0] = 1
    for i in range(max_n):
        fact[i + 1] = fact[i] * (i + 1) % mod

    inv_fact[-1] = pow(fact[-1], mod - 2, mod)
    for i in reversed(range(max_n)):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

    def nCr_mod(n, r):
        res = 1
        while n or r:
            a, b = n % mod, r % mod
            if a < b:
                return 0
            res = res * fact[a] % mod * inv_fact[b] % mod * inv_fact[a - b] % mod
            n //= mod
            r //= mod
        return res

    return nCr_mod

nCr_mod = make_nCr_mod()

### CODE HERE

H, W, A, B = read_int_list()

ret = 0

def path(x, y):
    old_x, old_y = x,y
    global ret
    a = nCr_mod(x+y, x)
    x += 1
    x, y = H-x-1, W-y-1
    b = nCr_mod(x+y, x)
    # print(f"path 0 0 -> {old_x} {old_y}: {a}")
    # print(f"path {old_x+1} {old_y} -> {H-1} {W-1} : {b}")

    ret += a*b
    ret %= MODULUS
    

x = H - A - 1 
for y in range(B, W):
    path(x, y)
print(ret)