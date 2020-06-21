#!/usr/bin/env python3

def divmod2(n, d):
    a, b = divmod(n, d)
    if b == 0:
        return a-1, d
    return a,b

def base(n):
    ret = []
    while n > 0:
        n, d = divmod2(n, 26)
        ret += [chr(ord('a') + d - 1)]
    return ''.join(ret[::-1])

N = int(input())

print(base(N))