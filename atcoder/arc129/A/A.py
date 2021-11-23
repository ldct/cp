#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def f_slow(R, N):
    ret = 0
    for x in range(1, R+1):
        if x^N < N:
            ret += 1
    return ret

def g(a, b, UB):
    return max(0, min(b, UB)+1 - a)

    ret = 0
    for x in range(a, b+1):
        if x <= UB:
            ret += 1
    return ret

def f(R, N):
    ret = 0
    bin = "{0:b}".format(N)[::-1]
    for i, b in enumerate(bin):
        if b == '1':
            ret += g(1 << i, (1 << (i+1))-1, R)
    return ret

if True:
    N, L, R = read_int_tuple()
    print(f(R, N) - f(L-1, N))
else:
    for N in range(100):
        for R in range(100):
            if not (f(R, N) == f_slow(R, N)):
                print(R, N)

    print("ok")