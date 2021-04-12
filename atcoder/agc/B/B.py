#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from functools import lru_cache

def rem(V, i):
    return V[0:i] + V[i+1:]

@lru_cache(None)
def ans_slow(V):
    N = len(V) // 2
    V1 = V[:N]
    V2 = V[N:]

    ret = 0

    for i in range(N):
        candidate = V1[i] + ans_slow(rem(V1, i) + rem(V2, 0))
        ret = max(ret, candidate)
        candidate = V2[i] + ans_slow(rem(V1, N-1) + rem(V2, i))
        ret = max(ret, candidate)

    return ret

def ans(V):
    N = len(V) // 2
    V1 = V[:N]
    V2 = V[N:]

    way_to_get = dict()

    for i in range(N):
        score = V1[i] - V2[0]
        way_to_get[score] = ('left', i)
        score = V2[i] - V1[-1]
        way_to_get[score] = ('right', i)

    lr, i = way_to_get[max(way_to_get.keys())]

    if lr == 'left':
        # if len(V) == 4: print("choose left", i)
        return V1[i] + ans_slow(rem(V1, i) + rem(V2, 0))
    else:
        # if len(V) == 4: print("choose right", i)
        return V2[i] + ans_slow(rem(V1, N-1) + rem(V2, i))


if True:
    from itertools import product
    N = 4
    for p in product((0, 1), repeat=2*N):
        if sum(p) != N: continue
        # if ans_slow(p) == N: continue
        print(p, ans_slow(p))
elif True:
    import random
    N = 2
    for _ in range(100000):
        tc = tuple(random.randint(1, 5) for _ in range(2*N))
        if ans(tc) != ans_slow(tc):
            print(tc, ans(tc), ans_slow(tc))
            assert(False)
            break
else:
    input()
    V = read_int_tuple()

    print(ans(V))