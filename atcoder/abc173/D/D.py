#!/usr/bin/env python3

from collections import deque

input()
A = input().split(' ')
A = list(map(int, A))
A = sorted(A)[::-1]

d = deque()

ret = 0

for a in A:
    if len(d) == 0:
        d.append(a)
    else:
        ret += d.popleft()
        d.append(a)
        d.append(a)

print(ret)
