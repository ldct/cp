#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

import bisect

### CODE HERE

import random
N = 2*10**5
A = [random.randint(1, 10**12) for _ in range(N)]
queries = [(random.randint(1, 10**12), random.randint(1, 10**12)) for _ in range(N)]

print(N)
print(*A)
print(N)
for x, y in queries:
    print(x, y)