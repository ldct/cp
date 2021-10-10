#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import defaultdict

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

def time(c):
    if 0 not in c: return float("inf")
    c = c + c

    last_0 = None
    ret = 0
    for i in range(len(c)):
        if c[i] == 0:
            last_0 = i
        elif last_0 is not None:
            ret = max(ret, i-last_0)

    return ret

def expand(seed, L, D, N):
    ret = []
    for _ in range(L):
        ret += [seed]
        seed += D
        seed %= N
    return ret

def ans(D, A):
    N = len(A)
    uf = UnionFind(N)

    for i in range(N):
        uf.join(i, (i+D) % N)

    seeds = set()

    for i in range(N):
        seeds.add(uf.find(i))

    class_length = N // len(seeds)

    classes = [expand(seed, class_length, D, N) for seed in seeds]
    classes = [[A[i] for i in c] for c in classes]

    classes = [time(c) for c in classes]
    ret = max(classes)

    if ret == float("inf"): ret = -1
    return ret

for _ in range(read_int()):
    _, D = read_int_tuple()
    A = read_int_list()

    print(ans(D, A))