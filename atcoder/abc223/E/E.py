#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def cdiv(x, y):
    return x // y if x % y == 0 else x // y + 1

def ok2_fd(X, Y, A, B):
    assert(X > 0)
    assert(Y > 0)
    y1 = cdiv(A, X)
    y2 = cdiv(B, X)
    return y1 + y2 <= Y

def ok2(X, Y, A, B):
    return ok2_fd(X, Y, A, B) or ok2_fd(Y, X, A, B)

def ok3_fod(X, Y, A, B, C):
    y1 = cdiv(A, X)
    y2 = Y - y1
    if y2 <= 0: return False
    return ok2(X, y2, B, C)

def ok3(X, Y, A, B, C):
    for x, y in [(X, Y), (Y, X)]:
        for a, b, c in [
            (A, B, C),
            (A, C, B),
            (B, A, C),
            (B, C, A),
            (C, A, B),
            (C, B, A)
        ]:
            if ok3_fod(x, y, a, b, c):
                return True
    return False

print("Yes" if ok3(*read_int_tuple()) else "No")