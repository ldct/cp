#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def cdiv(x, y):
    return x // y if x % y == 0 else x // y + 1

def cmod(x, M):
    return M*cdiv(x, M)

def ok(gap, A, B):
    # whether there are 2 multiples of `gap` between A and B
    a = cmod(A, gap)
    b = a + gap
    return A <= a < b <= B

def ans(A, B):
    top = B-A+1
    for gap in range(B-A+1, 0, -1):
        if ok(gap, A, B): return gap
    assert(False)

A, B = read_int_tuple()
print(ans(A, B))