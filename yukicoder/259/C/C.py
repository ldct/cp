#!/usr/bin/env pypy3

import sys
from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

MODULUS = 1000000007

N, M = input().split()
N = int(N)
M = int(M)

def prefix1(row):
    ret = [1]
    for a in row:
        ret += [(ret[-1] * a) % MODULUS]
    return ret

def prefix2(A):
    prefixes = []
    for row in A:
        prefixes += [prefix1(row)]

    # transpose
    prefixes = list(zip(*prefixes))

    prefixes2 = []
    for row in prefixes:
        prefixes2 += [prefix1(row)]

    ret = list(zip(*prefixes2))

    # optional: chop
    ret = [row[1:] for row in ret][1:]

    return ret

A = []

for _ in range(N):
    row = input().split()
    row = list(map(int, row))
    A += [row]

TL = prefix2(A)
TR = prefix2([row[::-1] for row in A])
BL = prefix2(A[::-1])
BR = prefix2([row[::-1] for row in A][::-1])

def tl(r, c):
    if r == 0 or c == 0: return 1
    return TL[r-1][c-1]

def tr(r, c):
    c = (M-1-c)
    # print("tr", r, c)
    if r == 0 or c == 0: return 1
    return TR[r-1][c-1]

def bl(r, c):
    r = (N-1-r)
    if r == 0 or c == 0: return 1
    return BL[r-1][c-1]

def br(r, c):
    r = (N-1-r)
    c = (M-1-c)
    # print("br", r, c)
    if r == 0 or c == 0: return 1
    return BR[r-1][c-1]

def ans(r, c):
    r -= 1
    c -= 1

    return (tr(r, c)*tl(r, c)*bl(r, c)*br(r, c)) % MODULUS

Q = int(input())

for _ in range(Q):
    r, c = input().split()
    r = int(r)
    c = int(c)
    print(ans(r, c))
