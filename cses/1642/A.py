#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import defaultdict

### CODE HERE

def match(A, B):
    for a in A:
        for b in B:
            if len(set(a + b)) == 4:
                return ' '.join(map(str, a + b))
def ans(A):
    def groups(A):
        ret = defaultdict(list)
        for ii in range(len(A)):
            for jj in range(ii+1, len(A)):
                i,a = A[ii]
                j,b = A[jj]
                ret[a+b] += [(i, j)]
        return ret

    A = [(i+1, a) for i,a in enumerate(A)]

    left = groups(A)
    right = groups(A)

    for k in left:
        m = match(left[k], right[X-k])
        if m is not None:
            return m

    return "IMPOSSIBLE"

N, X = read_int_tuple()
A = read_int_list()

print(ans(A))
