#!/usr/bin/env python3

def ans(X):
    if X > 45: return -1

    ret = []

    d = 9
    while X > 0:
        if X >= d:
            ret = [d] + ret
            X -= d
            d -= 1
        else:
            ret = [X] + ret
            X = 0

    return int("".join(map(str,ret)))

def ans_slow(X):
    for i in range(10000000):
        candidate = str(i)
        if X == sum(map(int, candidate)) and len(candidate) == len(set(candidate)):
            return i
    return -1

for _ in range(int(input())):
    X = int(input())
    print(ans(X))
