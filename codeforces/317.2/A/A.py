#!/usr/bin/env python3

import sys

NA, NB = input().split()
K, M = input().split()
K, M = int(K), int(M)

A = list(map(int, input().split()))
B = list(map(int, input().split()))

if (A[K-1] < B[-M]):
    print('YES')
else:
    print('NO')