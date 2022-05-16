#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from functools import lru_cache

def argmin(d):
    # return the set of keys which minimize d[k]
    min_val = float("inf")
    for k in d:
        min_val = min(min_val, d[k])

    ret = []

    for k in d:
        if min_val == d[k]:
            ret += [k]

    return ret

def ans(t, children, candies):

    def closest(x, y, idx_candies):
        dist = dict()

        for i in idx_candies:
            X, Y = candies[i]
            dist[i] = (x - X)**2 + (y - Y)**2

        return argmin(dist)

    @lru_cache(None)
    def dp(idx_children, idx_candies):

        assert(len(idx_candies) == len(idx_children) + 1)

        if len(idx_children) == 0:
            return []

        for i in idx_children:
            x, y = children[i]

            for j in closest(x, y, idx_candies):

                # try to match i and j
                if j == 0: continue

                m = dp(idx_children - frozenset([i]), idx_candies - frozenset([j]))

                if m is not None:
                    return m + [(i, j)]

        return None

    return dp(
        frozenset(range(len(children))),
        frozenset(range(len(candies)))
    )

T = int(input())
for t in range(T):
    N = read_int()
    children = [read_int_tuple() for _ in range(N)]
    candies = [read_int_tuple() for _ in range(N+1)]
    r = ans(t, children, candies)
    if r is None:
        print("Case #" + str(t+1) + ": IMPOSSIBLE")
    else:
        print("Case #" + str(t+1) + ": POSSIBLE")
        for i, j in r[::-1]:
            print(i+1, j+1)
