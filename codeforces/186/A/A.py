#!/usr/bin/env python3

N = input()

a = int(N)

b = float("-inf")
if len(N) >= 1:
    b = list(N)
    del b[-1]
    b = int(''.join(b))

c = float("-inf")
if len(N) >= 2:
    c = list(N)
    del c[-2]
    c = int(''.join(c))

print(max(a, b, c))