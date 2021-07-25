#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from collections import deque

N, M = read_int_tuple()
neighbours = []
for _ in range(N):
    neighbours += [[]]

for _ in range(M):
    A, B = read_int_tuple()
    A -= 1
    B -= 1
    neighbours[A] += [B]
    neighbours[B] += [A]

distance = [10**6]*N
distance[0] = 0
num_shortest = [0]*N
num_shortest[0] = 1
visited = set()
visited.add(0)

worklist = deque([0])

while worklist:
    u = worklist.popleft()
    # print("visiting", u)
    for child in neighbours[u]:
        if child not in visited:
            worklist.append(child)
            visited.add(child)

        if distance[child] > distance[u] + 1:
            distance[child] = distance[u] + 1
            num_shortest[child] = num_shortest[u]
        elif distance[child] == distance[u] + 1:
            num_shortest[child] += num_shortest[u]

print(num_shortest[N-1] % (10**9+7))