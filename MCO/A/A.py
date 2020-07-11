#!/usr/bin/env python3

# https://codeforces.com/group/R2SERIff4f/contest/213171/problem/B

import array

input()

heights = input().split(' ')
heights = array.array('i', list(map(int, heights)))

max_height = -1
max_idx = None

for i, h in enumerate(heights):
    if h > max_height:
        max_height = h
        max_idx = i

ans = 0

max_height = -1

for i in range(max_idx-1, -1, -1):
    h = heights[i]
    if h > max_height:
        ans += 1
        max_height = h

max_height = -1

for i in range(max_idx+1, len(heights)):
    h = heights[i]
    if h > max_height:
        ans += 1
        max_height = h

print(ans)