#!/usr/bin/env pypy3

N = int(input())
ret = []
for i in range(1,N+1):
    if i % 2 == 1:
        ret += [i]
print(*ret)