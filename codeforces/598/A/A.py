#!/usr/bin/env python3
import sys


def powersOfTwo():
    i = 0
    while True:
        yield 2**i
        i += 1

T = int(input())

for _ in range(T):
    N = int(input())

    ans = N*(N+1)//2
    for p in powersOfTwo():
        if p > N:
            break
        ans -= 2*p

    print(ans)