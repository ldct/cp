#!/usr/bin/env python3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from scipy import optimize
import numpy
import math

def ans(N2, N3, N4):
    N6 = N3 // 2

    N1, N2, N3 = N2, N4, N6

    A_ub = [
        [2, 1, 0],
        [-1, 2, 1],
        [0, 0, 1]
    ]
    b_ub = [N1, N2, N3]

    r = optimize.linprog(
        [0, -1, -1],
        A_ub = A_ub,
        b_ub = b_ub,
        options = {
            'tol': 1e-20,
            'autoscale': True
        },
        method='revised simplex'
    )

    def f(a, b, c):
        if not all(numpy.dot(A_ub, [a, b, c]) <= b_ub): return -1
        if a < 0: return -1
        if b < 0: return -1
        if c < 0: return -1
        return b+c

    def opt(A, B, C):
        ret = -1
        for a in range(A-2, A+2):
            for b in range(B-2, B+2):
                for c in range(C-2, C+2):
                    ret = max(ret, f(a, b, c))
        return ret

    [a, b, c] = r.x
    a = math.floor(a)
    b = math.floor(b)
    c = math.floor(c)
    return opt(a, b, c)

if False:
    import random
    for _ in range(10000):
        def r():
            return random.randint(1, 10**15)
        args = [r(), r(), r()]
        if ans(*args) is None:
            print(args)
else:
    for _ in range(read_int()):
        print(ans(*read_int_list()))