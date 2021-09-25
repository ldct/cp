#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def fun(a, b):
    ret = "("*a + ")"*a + "()"*b
    return ret

def rev(r):
    ret = ""
    for c in r:
        if c == "(":
            ret += ")"
        else:
            ret += "("
    return ret[::-1]

def ans(N):
    ret = []
    for i in range(N):
        r = fun(i, N-i)
        ret += [r]
        ret += [rev(r)]
    ret = list(set(ret))
    if N == 2:
        ret += ["(())"]
    return ret[:N]

def balanced(b):
    i = 0
    for c in b:
        if i < 0: return False
        if c == "(":
            i += 1
        else:
            i -= 1
    return i == 0

if True:
    for _ in range(read_int()):
        for l in ans(read_int()): print(l)