#!/usr/bin/env pypy3

def ans(M, A):
    AS = set(A)
    for i in range(1,M):
        if i not in AS:
            return -1
    ret = len(A)
    for a in A:
        if a == M:
            ret -= 1
    return ret

T = int(input())

for _ in range(T):
    [N, M, *rest] = input().split(' ')
    M = int(M)
    A = input().split(' ')
    A = [int(a) for a in A if len(a)]
    print(ans(M, A))