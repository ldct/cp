#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

N = read_int()
K = read_int()

eligible = set()

for i in range(N):
    S = input()
    for j in range(N):
        if S[j] == '.':
            eligible.add((i, j))

FINAL = set()

from functools import lru_cache

visited = set()

def ans(chosen, remaining):
    if remaining == 0:
        FINAL.add(chosen)
    if remaining < 0: return
    if chosen in visited: return

    visited.add(chosen)

    for x, y in chosen:
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_x = x+dx
            new_y = y+dy
            p = (new_x, new_y)

            if p not in chosen and p in eligible:
                ans(chosen | frozenset([p]), remaining - 1)

for p in eligible:
    ans(frozenset([p]), K-1)

print(len(FINAL))
