#!/usr/bin/env python3

T = int(input())

FIRST_PLAYER = "Ashish"
SECOND_PLAYER = "Vivek"

def ans(A):
    N = len(A)
    M = len(A[0])

    num_rows = 0
    for i in range(N):
        if 1 not in A[i]:
            num_rows += 1

    A = list(zip(*A))

    num_cols = 0
    for i in range(M):
        if 1 not in A[i]:
            num_cols += 1
    
    parity = min(num_rows, num_cols)

    if parity % 2 == 0:
        return SECOND_PLAYER
    return FIRST_PLAYER

    return (num_rows, num_cols)

for t in range(T):
    n, m = input().split(' ')
    n = int(n)

    A = []
    for _ in range(n):
        row = input().split(' ')
        row = [int(x) for x in row]
        A += [row]

    print(ans(A))
    