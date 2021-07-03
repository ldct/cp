#!/usr/bin/env python3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

import math

### CODE HERE

def center(A):
    N = 0
    X = 0
    Y = 0
    for (x, y) in A:
        X += x
        Y += y
        N += 1
    X /= N
    Y /= N

    return [(x-X, y-Y) for x, y in A]
    return X, Y

def rot(p, d):
    (x, y) = p
    C = math.cos(math.radians(d))
    S = math.sin(math.radians(d))

    return C*x - S*y, S*x + C*y

def are_ints(p):
    return is_int(p[0]) and is_int(p[1])

def is_int(i):
    return abs(i - int(round(i))) < 0.01

def dist(p1, p2):
    (a, b) = p1
    (c, d) = p2
    return (c-a)**2 + (d-b)**2

def equal(arr1, arr2):
    # print(sorted(arr1))
    # print(sorted(arr2))

    for p1, p2 in zip(sorted(arr1), sorted(arr2)):
        if dist(p1, p2) > 0.1: return False
    return True

def ans(ins, out):
    ins = center(ins)
    out = center(out)

    for d in range(360):
        rotated = [rot(p, d) for p in ins]

        if equal(rotated, out): return "Yes"

    return "No"

if False:
    import random
    ins = [(random.randint(0, 10), random.randint(0, 10)) for _ in range(100)]
    out = [(random.randint(0, 10), random.randint(0, 10)) for _ in range(100)]
    print(ans(ins, out))

else:
    N = read_int()
    ins = []
    out = []
    for _ in range(N):
        ins += [read_int_tuple()]
    for _ in range(N):
        out += [read_int_tuple()]

    print(ans(ins, out))
