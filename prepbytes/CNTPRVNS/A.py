#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from collections import defaultdict

def ans(N, edges):
  neighbours = defaultdict(list)
  for u, v in edges:
    neighbours[u] += [v]
    neighbours[v] += [u]

  visited = [False]*N

  def dfs(u):
    visited[u] = True
    for v in neighbours[u]:
      if visited[v]: continue
      dfs(v)

  ret = 0
  for i in range(N):
    if visited[i]: continue
    ret += 1
    dfs(i)

  return ret

for _ in range(read_int()):
    N, M = read_int_tuple()
    edges = []
    for _ in range(M):
      u, v = read_int_tuple()
      edges += [(u-1, v-1)]
    print(ans(N, edges))