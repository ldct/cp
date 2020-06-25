#!/usr/bin/env pypy3

import array
from collections import defaultdict

T = int(input())

def ans(A):
    A = list(array.array('i', [a // 10**8 for a in A]))
    A = [0] + A
    for i in range(1, len(A)):
        A[i] += A[i-1]
        A[i] = A[i] % 10
    freqs = defaultdict(int)
    for a in A:
        freqs[a] += 1
    ret = 0
    for a in freqs:
        f = freqs[a]
        ret += f*(f-1)//2
    return ret

for _ in range(T):
    input()
    A = input().split(' ')
    A = [int(x) for x in A if len(x)]
    print(ans(A))