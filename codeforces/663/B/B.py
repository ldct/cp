#!/usr/bin/env pypy3

def ans(A):
    ret = 0
    for c in A[-1][:-1]:
        if c != 'R':
            ret += 1
    for row in A[:-1]:
        if row[-1] != 'D':
            ret += 1
    return ret

T = int(input())

for _ in range(T):
    n, m = input().split()
    n = int(n)
    m = int(m)

    A = []
    for _ in range(n):
        A += [input()]

    print(ans(A))
