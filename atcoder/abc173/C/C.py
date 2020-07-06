#!/usr/bin/env python3

from itertools import chain, combinations

def subsets(iterable, low=0, high=None):
    "subsets([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    if high is None:
        high = len(s)
    return chain.from_iterable(combinations(s, r) for r in range(low, high+1))

H, W, K = input().split(' ')

H = int(H)
W = int(W)
K = int(K)

A = []

for _ in range(H):
    row = input()
    A += [row]

# print(f"A={A}")

ret = 0

def ok(rows, cols, A):
    A = [list(row) for row in A]
    for x in rows:
        for y in range(W):
            A[x][y] = '.'
    for y in cols:
        for x in range(H):
            A[x][y] = '.' 
    
    return K == sum(sum(1 for r in row if r == '#') for row in A)

for h in subsets(range(0, H)):
    for w in subsets(range(0, W)):
        if ok(h, w, A):
            ret += 1        
            # print(f"{h} {w}")

print(ret)