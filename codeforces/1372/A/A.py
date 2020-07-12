#!/usr/bin/env pypy3

T = int(input())

for t in range(T):
    n = int(input())
    if n == 1:
        print(1)
    else:
        x = [1]*(n-1) + [3]
        print(*x)
