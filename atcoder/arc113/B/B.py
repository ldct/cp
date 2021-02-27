#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def order(A):
    A %= 10
    for x in range(2, 100):
        if pow(A, x, 10) == A:
            return x

def ans(A, B, C):
    BC = pow(B, C, order(A)-1)
    BC += order(A)-1
    return pow(A, BC, 10)

def ans_slow(A, B, C):
    BC = pow(B, C)
    return pow(A, BC, 10)

if False:
    for a in range(2, 3):
        for b in range(1, 20):
            for c in range(1, 20):
                if ans(a, b, c) != ans_slow(a, b, c):
                    print(a, b, c)
else:
    A, B, C = read_int_tuple()
    print(ans(A, B, C))
