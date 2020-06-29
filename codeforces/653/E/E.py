#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

N, K = input().split(' ')
N = int(N)
K = int(K)

alice_only = []
bob_only = []
both = []

for _ in range(N):
    t, a, b = input().split(' ')
    t = int(t)
    a = int(a)
    b = int(b)

    if a == 0 and b == 0: continue
    if a == 1 and b == 1: both += [t]
    if a == 1 and b == 0: alice_only += [t]
    if a == 0 and b == 1: bob_only += [t]

hybrid = []

alice_only = sorted(alice_only)
bob_only = sorted(bob_only)

for a, b in zip(alice_only, bob_only):
    hybrid += [a + b]

candidates = sorted(both + hybrid)

if len(candidates) < K:
    print(-1)
else:
    print(sum(candidates[0:K]))
