#!/usr/bin/env python3

def num_x(A, B, C, D, t):
    low = max(C - t, A);
    high = min(B, D - t);

    return max(0, high - low + 1);


def ans(A, B, C, D):
    ret = 0

    for t in range(0, D+1):
        nx = num_x(A, B, C, D, t)
        f = (C - max(B, t+1) + 1)
        if (nx > 0 and f > 0):
            ret += nx * f

    return ret

A, B, C, D = input().split(' ')
A = int(A)
B = int(B)
C = int(C)
D = int(D)

print(ans(A, B, C, D))