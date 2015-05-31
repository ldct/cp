#!/usr/bin/env python3

from collections import defaultdict
import sys

N, M = input().split(' ')
N, M = int(N), int(M)
A = input().split(' ')
A = list(map(int, A))
B = input().split(' ')
B = list(map(int, B))

if (sum(A) != sum(B)):
    print('NO')
    sys.exit(0)

neighbours = defaultdict(lambda: defaultdict(int))
flow = defaultdict(int)

def left(i):
    return 'l ' + str(i)

def right(i):
    return 'r ' + str(i)

for i in range(1, N+1):
    for j in range(1, N+1):
        flow[left(i), right(j)] = 0
        flow[right(i), left(j)] = 0

for i, capacity in enumerate(A):
    neighbours['source'][left(i + 1)] = capacity
for i, capacity in enumerate(B):
    neighbours[right(i + 1)]['sink'] = capacity
for i in range(1, N+1):
    neighbours[left(i)][right(i)] = float('inf')


for m in range(M):
    p, q = input().split(' ')
    p, q = int(p), int(q)
    neighbours[left(p)][right(q)] = float('inf')
    neighbours[left(q)][right(p)] = float('inf')

def search():
    visited = set()
    def dfs(v):
        if v in visited:
            return False
        if v == 'sink':
            return ['sink']
        visited.add(v)
        for n in neighbours[v]:
            capacity = neighbours[v][n]
            if capacity > 0:
                res = dfs(n)
                if res:
                    return [v] + res
    return dfs('source')


total_flow = 0

def augment_edge(a, b, amount):
    neighbours[a][b] -= amount
    neighbours[b][a] += amount
    flow[a, b] += amount

def augment(path):
    capacity = float('inf')
    for i in range(len(path) - 1):
        capacity = min(capacity, neighbours[path[i]][path[i+1]])
    # print('augment', path, capacity)
    for i in range(len(path) - 1):
        augment_edge(path[i], path[i+1], capacity)
    global total_flow
    total_flow += capacity

while True:
    res = search()
    if res is None:
        break
    else:
        augment(res)

if (total_flow == sum(A)):
    print("YES")
    for i in range(1, N+1):
        for j in range(1, N+1):
            print(flow[left(i), right(j)] - flow[right(j), left(i)], end=" ")
        print()
else:
    print("NO")