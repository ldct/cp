#!/usr/bin/env python3

input()
A = list(map(int, input().split()))

front_height = A[0]

ret = 0

for a in A[1:]:
    if a < front_height:
        ret += front_height - a
    front_height = max(front_height, a)

print(ret)