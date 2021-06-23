#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

import math

def lcm(a, b):
    return a*b // math.gcd(a, b)

def vau_factorial(p, k):
    # count maximum power of p that divides k!
    ret = 0
    while k:
        ret += (k // p)
        k //= p

    return ret

def vau(p, k):
    # p-adic valuation
    for i in range(100, 0, -1):
        if k % (p**i) == 0: return i
    return 0

def count(m, a, b):
    # number of multiples of m in a...b
    return b//m - (a-1)//m

def num(p, a, b):
    for r in range(100, 0, -1):
        if count(p**r, a, b) > 0:
            return r
    return 0

def ans(a, b):
    return min(num(2, a, b), num(5, a, b))

def ans_slow(a, b):
    ret = 1
    for i in range(a, b+1):
        ret = lcm(ret, i)
    return min(vau(2, ret), vau(5, ret))

### CODE HERE

a, b = read_int_tuple()
print(ans(a, b))