#!/usr/bin/env pypy3

def ans(n):
    if n % 2 == 0: return n // 2
    return (n+1) // 2

T = int(input())

for _ in range(T):
    n = int(input())
    print(ans(n))