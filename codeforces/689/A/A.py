#!/usr/bin/env pypy3

T = int(input())

S = "abc"*1000

def ans(N):
    return S[:N]

for _ in range(T):
    N, K = input().split()
    N = int(N)
    print(ans(N))