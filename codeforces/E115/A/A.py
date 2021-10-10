#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(row1, row2):
    visited = set()
    def dfs(x, y):
        if (x, y) in visited: return
        if not (0 <= x < 2): return
        if not (0 <= y < len(row1)): return
        if [row1, row2][x][y] == '1': return
        visited.add((x, y))
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                dfs(x+dx, y+dy)

    dfs(0, 0)
    return "YES" if (1, len(row1)-1) in visited else "NO"


    return row1, row2

for _ in range(read_int()):
    input()
    print(ans(input(), input()))