#!/usr/bin/env python3

def ans(A):
    A = [abs(a) for a in A]
    for i in range(1, len(A), 2):
        if i+1 < len(A):
            [p, q, r] = A[i-1:i+2]
            if p <= q <= r: A[i] = -A[i]
            elif p >= q >= r: A[i] = -A[i]
    return ' '.join([str(a) for a in A])

T = int(input())

for _ in range(T):
    input()
    A = input().split(' ')
    A = list(map(int, A))
    print(ans(A))