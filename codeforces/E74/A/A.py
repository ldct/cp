#!/usr/bin/env python3

T = int(input())

def ans(x, y):
    d = x - y
    if d == 1:
        return "NO"
    return "YES"

for _ in range(T):
    x, y = input().split(' ')
    x = int(x)
    y = int(y)
    print(ans(x, y))
