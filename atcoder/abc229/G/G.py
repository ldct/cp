#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def minMoves(A, k):
    A = [i for i, a in enumerate(A) if a]
    n = len(A)
    B = [0] * (n + 1)
    res = float('inf')
    for i in range(n):
        B[i + 1] = B[i] + A[i]
    for i in range(len(A) - k + 1):
        res = min(res, B[i + k] - B[k // 2 + i] - B[(k + 1) // 2 + i] + B[i])
    res -= (k // 2) * ((k + 1) // 2)
    return res

S = input()
S = [1 if c == "Y" else 0 for c in S]
K = read_int()

def ok(r):
    return minMoves(S, r) <= K

def ans():
    low = 0
    assert(ok(low))
    high = len(S)+10
    assert(not ok(high))

    while high - low > 2:
        mid = (low + high) // 2
        if ok(mid):
            low = mid
        else:
            high = mid

    for r in range(low, low+10):
        if not ok(r):
            return r-1

print(ans())