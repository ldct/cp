#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import defaultdict

### CODE HERE

H, W, N = read_int_list()
grid = []
for _ in range(N):
    grid += [read_int_tuple()]


cols = defaultdict(list)
rows = defaultdict(list)
int_of = defaultdict(int)

nodes = []

rowmax = [-100000]*(H+1)
colmax = [-100000]*(W+1)

for i, (x, y, n) in enumerate(grid):
    nodes += [(n, i)]
    cols[x] += [(n, i)]
    rows[y] += [(n, i)]

def group(vals):
    d = defaultdict(list)
    for k, v in vals:
        d[k] += [v]
    ret = []
    for k in d:
        ret += [(k, d[k])]
    ret.sort()
    return ret

groups = group(nodes)

groups.sort()
groups.reverse()

ans = defaultdict(int)

for n, nodes in groups:
    for i in nodes:
        x, y, _ = grid[i]
        ans[i] = max(0, 1 + rowmax[x], 1 + colmax[y])
    for i in nodes:
        x, y, _ = grid[i]
        rowmax[x] = max(rowmax[x], ans[i])
        colmax[y] = max(colmax[y], ans[i])

for i in range(N):
    print(ans[i])