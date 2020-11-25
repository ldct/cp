#!/usr/bin/env python3

for _ in range(int(input())):
    N = int(input())
    ret = list(range(2, N+1)) + [1]
    print(*ret)