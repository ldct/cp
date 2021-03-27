#!/usr/bin/env pypy3

from __future__ import division, print_function

import itertools
import sys

from itertools import permutations

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

from itertools import chain, combinations

def subsets(iterable, low=0, high=None):
    "subsets([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    if high is None:
        high = len(s)
    return chain.from_iterable(combinations(s, r) for r in range(low, high+1))

def solvable(A):
    if sum(list(map(sum, A))) == 0: return True

    N = len(A)
    while True:
        if sum(list(map(sum, A))) == 0: return True

        made_progress = False
        for i in range(N):
            if sum(A[i]) == -1:
                made_progress = True
                for j in range(N):
                    A[i][j] = 0
        A = list(zip(*A))
        A = list(map(list, A))
        for i in range(N):
            if sum(A[i]) == -1:
                made_progress = True
                for j in range(N):
                    A[i][j] = 0

        if not made_progress: break

    return sum(list(map(sum, A))) == 0


def ans(N,A,B):
    best = float("inf")
    for i in range(N):
        for j in range(N):
            if A[i][j] != -1:
                A[i][j] = 0
    points = []
    for i in range(N):
        for j in range(N):
            points += [(i, j)]
    for s in subsets(points):
        new_A = [row[:] for row in A]
        for (x,y) in s:
            new_A[x][y] = 0
        if solvable(new_A):
            cost = 0
            for (x,y) in s:
                cost += B[x][y]
            best = min(best, cost)
    return best

    for row in A: print(row)
    print()
    for row in B: print(row)
    return N

T = int(input())
for t in range(T):
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        A += [list(map(int, input().split()))]
    for _ in range(N):
        B += [list(map(int, input().split()))]
    input()
    input()
    print("Case #" + str(t+1) + ": " + str(ans(N,A,B)))
