#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def cover(S, p):
    return frozenset([s for s in S if s > p] + [p])

def ans(V):
    N = len(V)
    V = [0] + V

    cache = dict()

    def num(visible, remaining):
        if (visible, remaining) in cache: return cache[(visible, remaining)]

        if V[N - len(remaining)] != len(visible):
            return 0
        if len(remaining) == 0: return 1
        ret = 0
        for r in remaining:
            ret += num(cover(visible, r), remaining - frozenset([r]))

        cache[(visible, remaining)] = ret
        return ret

    return num(frozenset(), frozenset(range(N)))

if False:
    for _ in range(10):
        print(ans([1,2,3,4,5,6,7,8,9,10,11,12,13]))
else:
    T = int(input())
    for t in range(T):
        input()
        V = read_int_list()
        print("Case #" + str(t+1) + ": " + str(ans(V)))
