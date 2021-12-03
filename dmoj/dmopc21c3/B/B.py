#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from functools import lru_cache

### CODE HERE

def f(a, b, c, d):
    return a+1, a+b, c, c+d

def g(a, b, c, d):
    return c, a+b, a+1, c+d

def tup_fast(arr):
    ee, ec, oe, oc = 0,0,0,0
    for a in arr:
        if a == 0:
            ee, ec, oe, oc = ee+1, ec+ee, oe, oc+oe
        else:
            ee, ec, oe, oc = oe, ec+ee, ee+1, oc+oe
    return ee, ec, oe, oc

def tup_xy(x, y):
    ret = tupx_closed(x)
    for _ in range(y):
        ret = f(*ret)
    return ret

def p_fast(arr):
    ee, ec, oe, oc = tup_fast(arr)
    return ee+ec, oe+oc

def p_slow(arr):
    e, o = 0, 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            if sum(arr[i:j]) % 2 == 0:
                e += 1
            else:
                o += 1
    return e, o

def ans(N):
    candidates = {(0,0,0,0): ""}
    for _ in range(2*10**3+10):
        next_candidates = dict()
        for c in candidates:
            if c[0] + c[1] == N:
                return candidates[c]
            next_candidates[f(*c)] = candidates[c] + "0"
            next_candidates[g(*c)] = candidates[c] + "1"
        candidates = next_candidates

def ans_fast(N):
    for x in range(2*10**3):
        for y in range(2*10**3 - x):
            t = tup_xy(x, y)
            if t[0] + t[1] == N:
                return "1"*x + "0"*y

def tupx_closed(x):
    return (x // 2, (x-1)**2 // 4, (x+1)//2, x**2//4)

if False:
    for x in range(20):
        print(x, tupx_closed(x) == tup_fast([1]*x))
elif False:
    print(p_slow([1, 1, 0, 0, 1]))
else:
    N = read_int()
    a = ans_fast(N)
    if a is None:
        print(-1)
    else:
        print(len(a))
        print(*a)
