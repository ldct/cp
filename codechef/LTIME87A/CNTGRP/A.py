#!/usr/bin/env pypy3

from collections import Counter

MODULUS = 10**9+7

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()


def fac(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
        ret %= MODULUS
    return ret

print(fac(10**9))
import sys
sys.exit(0)

# def ncr(n, r):


def ans(N, M, A):
    
    # count number of trees

    A += [0]
    cA = Counter(A)

    k = list(cA.keys())

    ret = 1

    rows = []

    for i in range(1, max(k) + 1):
        rows += [cA[i]]
        if cA[i] == 0: return 0
        ret *= pow(cA[i-1], cA[i], MODULUS)
        ret %= MODULUS

    if M == N-1:
        return ret

    excess = M - (N-1)

    choices = 0
    for r in rows:
        choices += r*(r-1) // 2
        choices %= MODULUS

    return (ret*ncr(choices, excess)) % MODULUS


T = int(input())
for t in range(T):
    N, M = input().split()
    N = int(N)
    M = int(M)

    A = list(map(int, input().split()))

    print(ans(N, M, A))