#!/usr/bin/env python3

T = int(input())

def ans(A):
    A = [(a, i+1) for i,a in enumerate(A)]
    A = sorted(A)
    a, ai = A[0]
    b, bi = A[1]
    c, ci = A[-1]

    if a + b <= c:
        print(ai, bi, ci)
    else:
        print(-1)

for t in range(T):
    input()
    A = list(map(int, input().split()))
    ans(A)