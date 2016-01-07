#!/usr/bin/env python3

def transpose(grid):
    return [[grid[y][x] for y in range(len(grid))] for x in range(len(grid[0]))]

def preprocess(grid):
    st1 = [[x >= 1 and grid[y][x-1] == grid[y][x] == '.'
            for x in range(len(grid[0]))]
           for y in range(len(grid))]
    st2 = [[0 for x in range(len(st1[0]))] for y in range(len(st1))]
    for y in range(len(st1)):
        for x in range(len(st1[0])):
            st2[y][x] = ((st2[y-1][x] if y >= 1 else 0) +
                         (st2[y][x-1] if x >= 1 else 0) -
                         (st2[y-1][x-1] if y >= 1 and x >= 1 else 0) +
                         int(st1[y][x]))
    return st2

import pprint

h, w = [int(x) for x in input().split()]
grid = [input() for y in range(h)]
pre, pre2 = preprocess(grid), transpose(preprocess(transpose(grid)))
#print(len(pre), len(pre[0]), len(pre2), len(pre2[0]))
#pprint.pprint(pre)
#pprint.pprint(pre2)
q = int(input())
for qi in range(q):
    r1, c1, r2, c2 = [int(x) for x in input().split()]
    r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1
    """val = (pre[r2][c2] +
           (pre[r1-1][c1-1] if r1 >= 1 and c1 >= 1 else 0) -
           (pre[r2][c1-1] if c1 >= 1 else 0) -
           (pre[r1-1][c2] if r1 >= 1 else 0) +
           pre2[r2][c2] +
           (pre2[r1-1][c1-1] if r1 >= 1 and c1 >= 1 else 0) -
           (pre2[r2][c1-1] if c1 >= 1 else 0) -
           (pre2[r1-1][c2] if r1 >= 1 else 0))
    """
    """val = (pre[r2][c2] - pre[r2][c1] - pre[r1][c2] + pre[r1][c1] +
           pre2[r2][c2] - pre2[r2][c1] - pre2[r1][c2] + pre2[r1][c1])"""
    val = (pre[r2][c2] +
           (pre[r1-1][c1] if r1 >= 1 else 0) -
           (pre[r2][c1] if c1 >= 0 else 0) -
           (pre[r1-1][c2] if r1 >= 1 else 0) +
           pre2[r2][c2] +
           (pre2[r1][c1-1] if c1 >= 1 else 0) -
           (pre2[r2][c1-1] if c1 >= 1 else 0) -
           (pre2[r1][c2] if r1 >= 0 else 0))
    """print(val, pre[r2][c2] +
           (pre[r1-1][c1] if r1 >= 1 else 0) -
           (pre[r2][c1] if c1 >= 0 else 0) -
           (pre[r1-1][c2] if r1 >= 1 else 0),
          pre2[r2][c2] +
           (pre2[r1][c1-1] if c1 >= 1 else 0) -
           (pre2[r2][c1-1] if c1 >= 1 else 0) -
           (pre2[r1][c2] if r1 >= 0 else 0), r1, c1, r2, c2)"""
    print(val)