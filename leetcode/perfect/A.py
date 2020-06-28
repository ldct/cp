#!/usr/bin/env pypy3

def ans(n, tried):
    if n < 0: return float("-inf")
    if n == 0: return 0
    if n == 1: return 1
    if tried >= 4: return 4
    i = 1
    ret = float("inf")
    while True:
        if i*i > n: return ret
        ret = min(ret, 1+ans(n-i*i, tried+1))
        i += 1
