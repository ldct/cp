#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def ans_1(E):
    S1 = sum(E)
    S2 = sum(e**2 for e in E)

    if S1**2 == S2: return 0

    if S1 == 0: return None

    if S2 % S1 != 0: return None

    twice_k = S2//S1 - S1

    if twice_k % 2 != 0: return None
    return twice_k // 2

    return E

def corr(a):
    ret = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            ret += a[i]*a[j]
    return ret

def balanced(arr):
    S1 = sum(arr)
    S2 = sum(e**2 for e in arr)

    return S1**2 == S2

def ans_2(E):
    S1 = sum(E)
    G = -corr(E)

    q = 1 - S1
    p = G - S1*q

    assert(balanced(E + [p, q]))

    return f"{p} {q}"


def ans(K, E):
    if K == 1: return ans_1(E)
    else: return ans_2(E)
    return E

if False:
    import random
    for _ in range(10000):
        tc = [random.randint(-5, 5) for _ in range(3)]
        if corr(tc) == 0:
            assert(balanced(tc))
    pass
else:
    T = int(input())
    for t in range(T):
        N, K = read_int_tuple()
        E = read_int_list()

        r = ans(K, E)
        if r is None: r = "IMPOSSIBLE"
        print("Case #" + str(t+1) + ": " + str(r))
