#!/usr/bin/env python3

T = int(input())

def ans(n):
    l = len(n)
    ret = []
    for i, d in enumerate(n):
        if d == '0': continue
        ret += [d + '0'*(l - i - 1)]

    print(len(ret))
    print(' '.join(ret))

for t in range(T):
    n = input()
    ans(n)