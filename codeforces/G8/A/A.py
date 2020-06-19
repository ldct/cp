#!/usr/bin/env pypy3

def ans(a, b, n):
    if max(a, b) > n: return 0
    return 1 + ans(a + b, max(a, b), n)

T = int(input())

for _ in range(T):
    a, b, n = input().split(' ')
    a = int(a)
    b = int(b)
    n = int(n)

    print(ans(a, b, n))
