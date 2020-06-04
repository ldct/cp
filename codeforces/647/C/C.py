#!/usr/bin/env python3

def diff(a, b):
    masked = a^b
    s = "{0:b}".format(masked)
    ret = len([c for c in s if c == "1"])
    return ret

def ans(n):
    ret = 0
    for i in range(0, n):
        ret += diff(i, i+1)
    return ret

def fast_ans(n):
    s = "{0:b}".format(n)
    return 2*n - len([c for c in s if c == "1"])

T = int(input())
for t in range(T):
    n = int(input())
    print(fast_ans(n))