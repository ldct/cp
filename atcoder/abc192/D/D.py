#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from functools import lru_cache

def ans_slow(X, M):
    if X == 1: return 1

    S = list(map(int, str(X)))[::-1]

    @lru_cache(None)
    def ok(b):
        ret = 0
        for i in range(len(S)):
            ret += S[i]*(b**i)
            if ret > M: return False
        return ret

    ret = set()
    for t in range(int(max(S))+1, 10000):
        if ok(t):
            ret.add(ok(t))
    return len(ret)

def ans(X, M):
    if X == 1: return 1
    if len(str(X)) == 1:
        if X <= M: return 1
        return 0

    S = list(map(int, str(X)))[::-1]

    @lru_cache(None)
    def ok(b):
        ret = 0
        for i in range(len(S)):
            ret += S[i]*(b**i)
            if ret > M: return False
        return True

    start = int(max(S)) + 1

    low = start
    high = M+9

    if not ok(low): return 0
    if ok(high): assert(False)

    while high - low > 2:
        assert(ok(low))
        assert(not(ok(high)))

        mid = (low + high) // 2
        if ok(mid):
            low = mid
        else:
            high = mid


    for end in range(low, low+9):
        if not(ok(end)):
            return end - start

    assert(False)

if False:
    for X in range(1, 100):
        for M in range(1, 100):
            if not(ans(X, M) == ans_slow(X, M)):
                print(X, M, ans_slow(X, M))

else:
    X = read_int()
    M = read_int()

    print(ans(X, M))