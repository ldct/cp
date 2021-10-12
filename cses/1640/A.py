#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

import bisect

### CODE HERE

def find2(target, A):
    candidates = [i for i in range(len(A)) if A[i] == target]
    return candidates[0:2]

def ans(X, A):
    if X % 2 == 0:
        if (A.count(X // 2)) >= 2:
            x, y = find2(X//2, A)
            return f"{x+1} {y+1}"
    old_A = A[:]
    A.sort()
    for i in range(len(A)):
        target = X - A[i]
        if target == A[i]: continue
        j = bisect.bisect_left(A, target)
        try:
            if A[i] + A[j] == X:
                ii = old_A.index(A[i])
                jj = old_A.index(A[j])
                return f"{ii+1} {jj+1}"
        except IndexError:
            continue
    return "IMPOSSIBLE"

N, X = read_int_tuple()
A = read_int_list()

print(ans(X, A))
