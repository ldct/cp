#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from math import gcd

### CODE HERE

def euclid(a,b):
    if b == 0: return 1,0,a
    y,x,d = euclid(b, a%b)
    y -= a//b*x
    return x,y,d

def crt(a, m, b, n):
    if (n > m):
        a,b = b,a
        m,n = n,m
        x,y,g = euclid(m,n)
        assert((a - b) % g == 0)
        x = (b - a) % n * x % n / g * m + a
        if x >= 0:
            return x
        return x + m*n//g


def intersect(a, b, c, d):
    # find r such that aZ + b cap cZ + d = lcm(a, c)Z + r
    if (b - d) % gcd(a, c) != 0:
        return None
    return crt(b,a,d,c)

def ans(X, Y, P, Q):
    L1 = 2*(X+Y)
    L2 = P+Q
    for y in range(X, X+Y):
        for p in range(P, P+Q):
            # y, y + L1, y + 2L1, ...
            # p, p + L2, p + 2L2, ...
            print(intersect(L1, y, L2, p))

for _ in range(read_int()):
    print(ans(*read_int_tuple()))