#!/usr/bin/env python3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

from collections import defaultdict

N, D = input().split(' ')
N = int(N)
D = int(D)

A = []
for _ in range(N):
    A += [int(input())]

ans = dict()

sorted_A = sorted(A)
set_A = sorted(list(set(A)))

i = 0
for a in set_A:
    while a - sorted_A[i] >= D: i += 1
    ans[a] = i

for a in A:
    print(ans[a])