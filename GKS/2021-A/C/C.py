#!/usr/bin/env python2

from __future__ import division, print_function

import itertools
import sys, random

from heapq import *

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

def ans(R, C, arr):
    old_arr = [row[:] for row in arr]

    visited = []
    for _ in range(R):
        visited += [[0]*C]

    worklist = []
    for i in range(R):
        for j in range(C):
            worklist += [(-arr[i][j], i, j)]
    heapify(worklist)

    while len(worklist):
        (_, x, y) = heappop(worklist)
        if visited[x][y]: continue
        visited[x][y] = 1

        n = arr[x][y]

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_x = x + dx
            new_y = y + dy

            if not (0 <= new_x < R): continue
            if not (0 <= new_y < C): continue

            if arr[new_x][new_y] < n-1:
                arr[new_x][new_y] = n-1
                heappush(worklist, (-(n-1), new_x, new_y))

    ret = 0
    for i in range(R):
        for j in range(C):
            ret += arr[i][j] - old_arr[i][j]

    return ret

# R = 300
# C = 300
# tc = []
# for _ in range(R):
#     tc += [[random.randint(5,100) for _ in range(C)]]
# print(ans(R, C, tc))
# sys.exit()

T = int(input())
for t in range(T):
    R,C = input().split()
    R = int(R)
    C = int(C)
    arr = []
    for _ in range(R):
        arr += [list(map(int, input().split()))]
    print("Case #" + str(t+1) + ": " + str(ans(R, C, arr)))
