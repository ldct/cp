#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import defaultdict

def missing(arr):
    s = set(arr)
    for i in range(0, 100):
        if i not in s: return i
    assert(False)

def inv(arr):
    arr = [(a, i) for i,a in enumerate(arr)]
    arr.sort()
    return [i for (a,i) in arr]

def swap(arr, i, j):
    ret = list(arr[:])
    ret[i], ret[j] = ret[j], ret[i]
    return tuple(ret)

def get_idx(arr, target):
    for i in range(len(arr)):
        if arr[i] == target: return i
    assert(False)

def search_neighbours(state):
    ret = []
    u = get_idx(state, 8)
    for v in neighbours[u]:
        ret += [swap(state, u, v)]
    return tuple(ret)

### CODE HERE

neighbours = defaultdict(list)

M = read_int()
for _ in range(M):
    u, v = read_int_tuple()
    u -= 1
    v -= 1
    neighbours[u] += [v]
    neighbours[v] += [u]

p = [r-1 for r in read_int_list()]

p += [missing(p)]

p = tuple(inv(p))

visited = set([p])
curr_level = [p]

ans = None
t = 0

while True:
    if tuple(range(9)) in curr_level:
        ans = t
        break
    if len(curr_level) == 0: break
    next_level = []
    for s in curr_level:
        for n in search_neighbours(s):
            if n in visited: continue
            visited.add(n)
            next_level += [n]

    curr_level = next_level
    t += 1

if ans is None: ans = -1
print(ans)