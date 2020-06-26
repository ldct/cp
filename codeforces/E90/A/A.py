#!/usr/bin/env pypy3

def ans(a, b, c):
    r1 = -1
    r2 = -1

    if a < c: r1 = 1
    if c/b < a: r2 = b

    return r1, r2

T = int(input())

for _ in range(T):
    a, b, c = input().split(' ')
    a = int(a)
    b = int(b)
    c = int(c)

    print(*ans(a, b, c))
