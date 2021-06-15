#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

MODULUS = 10**9+7

from itertools import product
from functools import lru_cache

def co_slow(N):
    def good(p):
        if p[0] == -1: return False
        for i in range(len(p)-1):
            if p[i] == -1 and p[i+1] == -1: return False
        return True

    ret = [0]*N
    for p in product([1, -1], repeat=N):
        if good(p):
            for i in range(len(p)):
                ret[i] += p[i]

    return ret

@lru_cache(None)
def f(n):
    if n < 2: return n
    return (f(n-1) + f(n-2)) % MODULUS

@lru_cache(None)
def l(n):
    if n == 0: return 1
    if n == 1: return 3
    return (l(n-1) + l(n-2)) % MODULUS

for i in range(10**5):
    f(i)
    l(i)

def fib(a, b, n):
    if n == 0: return a
    if n == 1: return b
    return f(n-1)*a + f(n)*b


def co_fast(n):
    if n == 1: return [1]
    ret = []
    ret += [f(n+1), f(n-2)]

    while len(ret) != n:
        k = len(ret)
        ret += [fib(f(k-1), l(k-1), n-1-k)]
    return ret


for N in range(2, 16):
    assert(co_fast(N) == co_slow(N))

N = read_int()
A = read_int_list()

ret = 0
for a, b in zip(A, co_fast(N)):
    ret += a*b
    ret %= MODULUS

print(ret)