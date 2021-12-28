#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left

### CODE HERE

class UnionFind:
    def __init__(self, N):
        self.parent = dict()
        for i in range(N):
            self.parent[i] = i

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def join(self, a, b):
        self.parent[self.find(b)] = self.find(a)

N = read_int()
P = [p-1 for p in read_int_list()]
M = read_int()

reachable = UnionFind(N)

for _ in range(M):
    a, b = read_int_list()
    a -= 1
    b -= 1

    reachable.join(a, b)

def ans():
    for i in range(N):
        if P[i] != i and reachable.find(i) != reachable.find(P[i]):
            print(-1)
            return
    print("ok")

ans()