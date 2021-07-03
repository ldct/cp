#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import defaultdict

### CODE HERE

def solve(A):
    A = A[:]
    indexes = defaultdict(list)
    for i, a in enumerate(A):
        indexes[a] += [i]

    for a in indexes:
        indexes[a] = sorted(indexes[a])

    best_gap = float("inf")

    for a in indexes:
        [i, j] = indexes[a]
        best_gap = min(best_gap, j-i)

    for a in indexes:
        [i, j] = indexes[a]
        if j-i == best_gap:
            cost = j-i
            del A[j]
            del A[i]
            return cost, A

def ans_slow(A):
    ret = 0
    while len(A):
        cost, A = solve(A)
        ret += cost
    return ret

def cost(elems):
    freq = defaultdict(int)
    for e in elems:
        freq[e] += 1
        freq[e] %= 2
    ret = 0
    for k in freq:
        ret += freq[k]
    return ret

def ans(A):
    N = len(A) // 2

    A = A[:]
    indexes = defaultdict(list)
    for i, a in enumerate(A):
        indexes[a] += [i]

    swap = 0

    for i in range(1, N+1):
        l, r = sorted(indexes[i])
        elems = defaultdict(list)
        for j in range(l+1, r):
            elems[i] += [A[j]]
        swap += cost(elems[i])

    return N + swap//2

N = read_int()
A = read_int_list()

print(ans(A))
