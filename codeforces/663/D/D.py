#!/usr/bin/env pypy3

from sys import stdin, stdout, exit
 
def input():
    return stdin.readline().strip()

def match_same(col):
    (a,b,c) = col
    if a==b and b == col:
        return 0
    return 1

def match_exact(p, q):
    ret = 0
    for a,b in zip(p,q):
        if a != b:
            ret += 1
    return ret

def match_diff(col):

    (a,b,c) = col
    if a==b and b ==c: return 1

    return min(
        match_exact(col, (0,1,0)),
        match_exact(col, (1,0,1))
    )

def match_sd(col):
    return min(
        match_exact(col, (1,1,0)),
        match_exact(col, (0,0,1))
    )

def match_ds(col):
    return min(
        match_exact(col, (0,1,1)),
        match_exact(col, (1,0,0))
    )

def match(col, is_same):
    if is_same:
        return match_same(col)
    else:
        return match_diff(col)

def match_3(col, at_sd):
    if at_sd:
        return match_sd(col)
    else:
        return match_ds(col)

def ans_s(A):
    is_same = True
    ret = 0
    for col in A:
        ret += match(col, is_same)
        is_same = not is_same
    return ret

def ans_s2(A):
    is_same = True
    ret = 0
    for col in A:
        ret += match2(col, is_same)
        is_same = not is_same
    return ret

def ans_d(A):
    is_same = False
    ret = 0
    for col in A:
        ret += match(col, is_same)
        is_same = not is_same
    return ret

def ans_sd(A):
    if len(A[0]) != 3: return float("inf")

    at_sd = True
    ret = 0
    for col in A:
        ret += match_3(col, at_sd)
        at_sd = not at_sd
    return ret

def ans_ds(A):
    if len(A[0]) != 3: return float("inf")

    at_sd = False
    ret = 0
    for col in A:
        ret += match_3(col, at_sd)
        at_sd = not at_sd
    return ret

def ans(A, n):
    if n == 2:
        return min(ans_s2(A), ans_d2(A))
    else:
        return min(ans_s(A), ans_d(A), ans_sd(A), ans_ds(A))

n, m = input().split()
n = int(n)
m = int(m)

A = []
for _ in range(n):
    A += [input()]

if n >= 4:
    A = [tuple(map(int, row)) for row in A]

    print(-1)
    exit(0)

if n == 1:
    print(0)
    exit(0)

A = zip(*A)

A = [list(map(int, row)) for row in A]

print(ans(A, n))
