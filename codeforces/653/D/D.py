#!/usr/bin/env pypy3

from collections import Counter

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

def ans(A, K):
    A = [a % K for a in A if a % K > 0]

    if len(A) == 0: return 0
    
    A = Counter(A)

    ret = float("-inf")

    for cc in A:
        ret = max(ret, (A[cc] - 1)*K + K - cc + 1)

    return ret

T = int(input())

for _ in range(T):
    N, K = input().split(' ')
    K = int(K)
    A = input().split(' ')
    A = list(map(int, A))

    print(ans(A, K))