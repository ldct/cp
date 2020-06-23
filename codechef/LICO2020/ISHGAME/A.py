#!/usr/bin/env python3

T = int(input())

def ans(a, b):
    ret = []
    b = set(b)
    for c in a:
        if c not in b:
            ret += [c]
    return ''.join(ret)

for _ in range(T):
    a = input()
    b = input()

    print(ans(a, b))
