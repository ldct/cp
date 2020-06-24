#!/usr/bin/env python3

T = int(input())

for _ in range(T):
    n = int(input())
    if n % 4 == 0:
        print("YES")
    else:
        print("NO")