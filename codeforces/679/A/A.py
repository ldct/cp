#!/usr/bin/env pypy3

def ans(A):
    N = len(A) // 2
    B = []
    for i in range(N):
        [x, y] = A[2*i:2*i+2]
        B += [-y, x]
    print(*B)

for _ in range(int(input())):
    input()
    A = list(map(int, input().split()))
    ans(A)