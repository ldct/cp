#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

N = 200
import random
edges = []
for _ in range(N*(2*N-1)):
    a = random.randint(1, 2*N)
    b = random.randint(1, 2*N)
    if a == b: continue
    edges += [tuple(sorted([a, b]))]
print(N, len(edges))
for a, b in edges:
    print(a, b)
