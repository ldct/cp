#!/usr/bin/env pypy3

import array

MAX_N = 10**5

ans = array.array('i', [MAX_N]*MAX_N)

ans[0] = 0

for i in range(1, MAX_N):
    s = str(i)
    for c in s:
        x = int(c)
        if x > 0 and i - x >= 0:
            ans[i] = min(ans[i], 1+ans[i - x])

print(ans[int(input())])
