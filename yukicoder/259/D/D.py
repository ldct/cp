#!/usr/bin/env pypy3

from collections import defaultdict, Counter

import sys
from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

MODULUS = 1000000007

N, M, K = input().split()

K = int(K)

A = list(map(int, input().split()))
B = list(map(int, input().split()))

def prefix(N):
    ret = [0]
    for n in N:
        ret += [ret[-1] ^ n]
    return ret

if True:
    import random
    A = [random.randint(0, 1025) for _ in range(2*10**5)]
    B = [random.randint(0, 1025) for _ in range(2*10**5)]

A = prefix(A)
B = prefix(B)

print("prefix done")

cA = Counter()
cB = Counter()

fA = defaultdict(int)
fB = defaultdict(int)

for a in A: # O(2*10**5)
    for k in cA: # O(1024)
        fA[a^k] += cA[k]
        fA[a^k] %= MODULUS
    cA[a] += 1

for b in B: # O(2*10**5)
    for k in cB: # O(1024)
        fB[b^k] += cB[k]
        fB[b^k] %= MODULUS
    cB[b] += 1

print("pairs done")

ans = 0

for i in range(1025):
    j = i^K
    ans += fA[i]*fB[j]
    ans %= MODULUS

print(ans)