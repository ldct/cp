#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def up(N):
    while N % 10 == 0:
        N = N // 10

    ret = 1
    while N % 2 == 0:
        N = N // 2
        ret *= 5

    while N % 5 == 0:
        N = N // 5
        ret *= 2

    if N != 1: return None

    return ret

import math

def ans(A, B):
    g = math.gcd(A, B)
    A //= g
    B //= g
    big = up(B)
    if big is None: return -1

    A *= big
    B *= big

    ret = len(str(B))-1
    # return f"{A} / {B} = {A/B} = {ret}"
    return ret

def ans_slow(A, B):
    S = str(A/B).split(".")[-1]
    if len(S) > 5: return -1
    return len(S)

if False:
    print(ans(2, 4))
    print(ans_slow(2, 4))
elif False:
    for A in range(1, 6):
        for B in range(A+1, 6):
            if not (ans(A, B) == ans_slow(A, B)):
                print(A, B, ans(A, B), ans_slow(A, B))
else:
    for _ in range(read_int()):
        A, B = read_int_tuple()
        print(ans(A, B))