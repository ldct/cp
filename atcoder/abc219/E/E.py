#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import chain, combinations

def subsets(iterable, low=0, high=None):
    "subsets([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    if high is None:
        high = len(s)
    return chain.from_iterable(combinations(s, r) for r in range(low, high+1))

### CODE HERE

A = []
for _ in range(4):
    A += [read_int_list()]

coords = [(i, j) for i in range(4) for j in range(4)]

def ok(p):


    p = set(p)

    for i in range(4):
        for j in range(4):
            if A[i][j] == 1 and (i, j) not in p: return False

    visited = set()

    def dfs(x, y):
        if (x, y) in visited: return
        if (x, y) not in p: return
        if not (0 <= x < 4): return
        if not (0 <= y < 4): return

        visited.add((x, y))

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x = x+dx
            new_y = y+dy
            dfs(new_x, new_y)

    for x, y in p:
        dfs(x, y)
        break

    return len(p) == len(visited)

ret = 0
for p in subsets(coords):
    if ok(p):
        print(p)
        ret += 1

print(ret)