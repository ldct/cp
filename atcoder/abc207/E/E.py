#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

MODULUS = 10**9 + 7
from functools import lru_cache

def ans(A):
    prefixes = [0]
    for a in A: prefixes += [prefixes[-1] + a]

    @lru_cache(None)
    def dp(i, start):
        if i == len(A): return 1

        ret = 0
        for j in range(i+1, len(A)+1):
            if (prefixes[j] - prefixes[i]) % start == 0:
                ret += dp(j, start+1)
                ret %= MODULUS
        return ret

    return dp(0, 1)

if True:
    import random
    A = [random.randint(1, 10**6) for _ in range(3000)]
    print(len(A))
    print(*A)
else:
    input()
    A = read_int_list()
    print(ans(A))