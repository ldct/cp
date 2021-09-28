#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from functools import lru_cache
import sys

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
FACTORS = [-1]*62

def bits_factorize(n):
    ret = 0
    for i,p in enumerate(PRIMES):
        if n % p == 0:
            ret |= (1 << i)
    return ret

for i in range(1, 62):
    FACTORS[i] = bits_factorize(i)

def clashes(avoid, k):
    return avoid & FACTORS[k] > 0

def ans(A):
    @lru_cache(None)
    def min_score(i, avoid):
        if i == len(A): return (0, [])
        ret_score = 10**6
        ret_seq = None

        for k in range(1, 2*A[i]+1):
            if clashes(avoid, k): continue
            score, seq = min_score(i+1, avoid | FACTORS[k])
            if abs(k-A[i]) + score < ret_score:
                ret_score = abs(k-A[i])+score
                ret_seq = seq + [k]
        return ret_score, ret_seq

    ret = min_score(0, 0)
    return (ret[0], ret[1][::-1])

if False:
    import random
    tc = [random.randint(1, 30) for _ in range(10)]
    print(tc)
    print(ans(tc))
else:
    input()
    A = read_int_list()
    print(ans(A))