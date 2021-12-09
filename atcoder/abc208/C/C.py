#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from math import factorial, gcd
from collections import Counter, defaultdict

### CODE HERE

N, K = read_int_tuple()
A = read_int_list()
A = [(a, i) for (i,a) in enumerate(A)]
A.sort()
ret = [K // N]*N
K %= N
for i in range(K):
    ret[i] += 1
ret = [(A[i][1], ret[i]) for i in range(N)]
ret.sort()
ret = [r[1] for r in ret]
print('\n'.join(map(str,ret)))