#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from collections import defaultdict

[N, M] = read_int_list()
A = read_int_list()
children = defaultdict(list)
for _ in range(M):
    x, y = read_int_tuple()
    x -= 1
    y -= 1
    children[x] += [y]

max_reachable = [float("-inf") for i in range(len(A))]

for u in range(N,-1,-1):
    for v in children[u]:
        max_reachable[u] = max(max_reachable[u], max_reachable[v], A[v])

# print(A)
# print(max_reachable)

profit = [mr - c for mr, c in zip(max_reachable, A)]
print(max(profit))