#!/usr/bin/env pypy3

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

def factorize(n):
    N = n
    ret = []
    i = 2
    while i<=n:
        if i * i > N:
            ret.append(n)
            break
        if n%i==0:
            ret.append(i)
            n//= i
        else:
            i+=1
    return ret

def is_prime(x):
    return len(factorize(x)) == 1

def partitions(arr):
    ret = []
    n = len(arr)

    for partition_index in range(2 ** (n-1)):
        partition = []
        subset = []

        for position in range(n):
            subset.append(arr[position])

            if 1 << position & partition_index or position == n-1:
                partition.append(subset)
                subset = []

        ret += [partition]
    return ret

def product(lst):
    p = 1
    for i in lst:
        p *= i
    return p

def multiplicative_partitions(n):
    from more_itertools import set_partitions

    ret = []
    for p in set_partitions(factorize(n)):
        m = list(map(product, p))
        ret += [tuple(sorted(m))]
    ret = list(set(ret))
    ret.sort()
    return ret

def ans_slow(x, d):
    def good(n):
        return n % d == 0
    def beautiful(n):
        return good(n) and n % (d*d) != 0

    def valid(p):
        return all(map(beautiful, p))

    ret = 0
    for p in multiplicative_partitions(x):
        if valid(p):
            ret += 1

    return ret >= 2

def ans(x, d):
    if is_prime(d):
        a = []
        while x % d == 0:
            x //= d
            a += [d]
        b = factorize(x)

        if len(a) <= 1: return False
        if len(b) <= 1: return False
        return True

    a = []
    while x % d == 0:
        x //= d
        a += [d]
    b = factorize(x)

    if len(a) <= 1: return False
    if len(b) >= 2: return True

    if len(b) == 0:
        if len(a) <= 2: return False
        return True

    assert(len(b) == 1)

    b = b[0]
    if b*b == d:
        if len(a) <= 3: return False
        return True

    # a >= 2
    # b <= a

    assert(len(a) >= 2)
    return len(a) >= 3

if False:
    x, d = 3, 4
    print(ans_slow(x, d))
    print(ans(x, d))
elif True:
    for d in [2, 4, 6, 8]:
        for x in range(2, 1000):
            r = ans(x, d)
            if r == '?': continue
            if not (ans_slow(x ,d) == r):
                print(x, d, ans_slow(x, d), r)
else:
    for _ in range(read_int()):
        print("YES" if ans(*read_int_list()) else "NO")