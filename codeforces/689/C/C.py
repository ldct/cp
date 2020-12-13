#!/usr/bin/env pypy3

from sys import stdin, stdout

def input():
    return stdin.readline().strip()

T = int(input())

def ans(A, experiments):
    i = len(A)-1
    while i >= 0 and A[i] == i+1:
        i -= 1
    if i == -1: return 1.0

    chances = []

    for (r, p) in experiments:
        if r >= i:
            chances += [p]

    ret = 1.0
    for p in chances:
        ret *= (1-p)

    return 1-ret

for _ in range(T):
    N, M = input().split()
    N = int(N)
    M = int(M)

    A = list(map(int, input().split()))
    experiments = []
    for _ in range(M):
        r, p = input().split()
        experiments += [(int(r)-1, float(p))]

    print(ans(A, experiments))