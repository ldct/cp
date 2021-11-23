#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

import math

### CODE HERE

def score(S):
    ret = 0
    for i in range(len(S)+1):
        for j in range(i+1, len(S)+1):
            if int(S[i:j]) % 7 == 0:
                ret += 1
    return ret

def choose(x):
    return x*(x-1) // 2

def inv_choose(n):
    if n < 0: return None
    m = 1 + int(math.sqrt(8*n+1) - 1) // 2
    if choose(m) == n: return m

def sum3(N):
    # return a, b, c s.t. (a choose 2) + (b choose 2) + (c choose 2)

    B = int(math.sqrt(N) + 100)

    for a in range(1, B):
        for b in range(1, B):
            c = inv_choose(N - choose(a) - choose(b))
            if c is not None and c < B:
                assert(choose(a) + choose(b) + choose(c) == N)
                return a, b, c

    assert(False)

def ans(N):
    a, b, c = sum3(N)
    a -= 1
    b -= 1
    c -= 1

    A = a * "7"
    B = b * "7"
    C = c * "7"

    x = pow(5, c, 7)
    y = pow(5, c+1+b, 7)
    S = f"{A}{x}{B}{y}{C}"
    return S
    assert(score(S) == N)

print(ans(read_int()))
