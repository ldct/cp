#!/usr/bin/env pypy3

import math

input()
H = list(map(int, input().split()))

ret = [0]*len(H)

for i in range(len(H)-2, -1, -1):
    if H[i] >= H[i+1]:
        ret[i] = 1 + ret[i+1]

print(max(ret))