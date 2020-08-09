#!/usr/bin/env pypy3

T = int(input())

for _ in range(T):
    n = int(input())
    print(*range(1,n+1))
