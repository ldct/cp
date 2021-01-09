#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

import itertools

[N, K] = read_int_list()
T = []

for _ in range(N):
    T += [read_int_list()]

ret = 0
for p in itertools.permutations(range(1,N)):
    cost = 0
    pp = (0,) + p + (0,)
    for i in range(len(pp) - 1):
        a = pp[i]
        b = pp[i+1]
        cost += T[a][b]
    if cost == K:
        ret += 1

print(ret)