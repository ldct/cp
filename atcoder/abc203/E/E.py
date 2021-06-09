#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import defaultdict

### CODE HERE

xs = set()
pawns = defaultdict(list)

N, M = read_int_tuple()
for _ in range(M):
    x, y = read_int_tuple()
    xs.add(x)
    pawns[x] += [y]

xs = list(sorted(xs))

positions = set([N])

for x in xs:
    to_delete = set()
    to_add = set()

    for y in pawns[x]:
        to_delete.add(y)
        if y-1 in positions or y+1 in positions:
            to_add.add(y)

    for d in to_delete:
        if d in positions:
            positions.remove(d)
    for a in to_add:
        positions.add(a)

print(len(positions))