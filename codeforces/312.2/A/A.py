#!/usr/bin/env python3

import sys

N = int(input())

apples = []

for n in range(N):
    a, b = input().split(' ')
    a, b = int(a), int(b)
    apples.append((a, b))

apples.sort()

apples_left = [(a, b) for a, b in apples if a < 0]
apples_right = [(a, b) for a, b in apples if a > 0]

len_left = len(apples_left)
len_right = len(apples_right)

if (len_left == len_right):
    print(sum(b for a, b in apples))
    sys.exit(0)

if (len_left < len_right):
    # go right
    ans = 0
    ans += sum(b for a, b in apples_left)
    ans += sum(b for a, b in apples_right[:len_left + 1])
    print(ans)
    sys.exit(0)

if (len_left > len_right):
    # go left
    ans = 0
    ans += sum(b for a, b in apples_right)
    ans += sum(b for a, b in apples_left[-len_right-1:])
    print(ans)
    sys.exit(0)