#!/usr/bin/env python3

def ans(n, m):
    n, m = min(n, m), max(n, m)
    if n <= 2 and m <= 2:
        return "YES"
    if n == 1:
        return "YES"
    return "NO"

T = int(input())
for t in range(T):
    n, m = input().split(' ')
    n, m = int(n), int(m)
    print(ans(n, m))