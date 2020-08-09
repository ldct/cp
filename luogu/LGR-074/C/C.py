#!/usr/bin/env python3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

import sys

def ml(A, i):
    return sum(a^i for a in A)

def ok(A, i, limit):
    return ml(A, i) <= limit

def ans(A, limit):
    ub = 2*max(A + [limit])

    for i in range(ub, -1, -1):
        if ok(A, i, limit):
            return i
    
    return -1

input()
A = list(map(int, input().split()))
Q = int(input())
queries = []
for _ in range(Q):
    queries += [int(input())]

if Q == 1:
    print(ans(A, queries[0]))
    sys.exit(0)

#ST2

ub = 5*10**3
if len(A) > 10**3:
    ub=2*10**3

ml_of = dict()
for i in range(ub, -1, -1):
    ml_of[i] = ml(A, i)

def ans2(ml_of, limit):
    for i in range(ub, -1, -1):
        if ml_of[i] <= limit:
            return i
    return -1

for limit in queries:
    print(ans2(ml_of, limit))
