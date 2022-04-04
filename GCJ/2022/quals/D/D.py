#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import defaultdict
from itertools import permutations

def score(F, P, order):
    N = len(F)
    visited = set([0])

    def visit(u):
        if u in visited:
            return 0
        visited.add(u)
        return max(F[u], visit(P[u]))

    ret = 0
    for u in order:
        a = visit(u)
        ret += a
    return ret

def ans_dfs(F, P):
    children = defaultdict(list)

    N = len(F)
    F = [0] + F
    P = [-1] + P

    for i, p in enumerate(P):
        if p == -1: continue
        children[p] += [i]

    def dfs(u):
        if len(children[u]) == 0: return [(F[u], 0)]
        cv = []

        for v in children[u]:
            cv += [dfs(v)]

        maxes = [max(sum(k) for k in t) for t in cv]
        cm = [sum(maxes) - m for m in maxes]

        ret = []
        for a, b in zip(cv, cm):
            for (p, q) in a:
                ret += [(max(p, F[u]), q + b)]

        return ret

    return max(sum(t) for t in dfs(0))


def ans_slow(F, P):
    children = defaultdict(list)

    N = len(F)
    F = [0] + F
    P = [-1] + P

    for i, p in enumerate(P):
        if p == -1: continue
        children[p] += [i]

    terminals = []
    for i in range(1, N+1):
        if len(children[i]) == 0:
            terminals += [i]

    ret = 0
    for order in permutations(terminals):
        ret = max(ret, score(F, P, order))

    return ret

if False:
    P = [0, 1, 2, 2]
    F = [1, 1, 2, 3]
    print(ans_slow(F, P))
    print(ans_dfs(F, P))
elif False:
    import random
    for _ in range(1000):
        P = [0, 1, 1, 2, 2, 3, 3]
        F = [random.randint(1, 5) for _ in range(len(P))]
        if not (ans_dfs(F, P) == ans_slow(F, P)):
            print(F, P)
            break
elif False:
    import random
    for _ in range(1000):
        F = [random.randint(1, 5) for _ in range(5)]
        P = [0, 1, 2, 2, 1]
        if not (ans_dfs(F, P) == ans_slow(F, P)):
            print(F, P)
            break
else:
    T = int(input())
    for t in range(T):
        input()
        F = read_int_list()
        P = read_int_list()
        print("Case #" + str(t+1) + ": " + str(ans_dfs(F, P)))
