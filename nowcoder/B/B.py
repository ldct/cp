#!/usr/bin/env pypy3

n = int(input())

for i in range(1,n+1):
    print(*list(range(1,i+1)))
