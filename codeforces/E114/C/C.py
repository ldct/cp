#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

import bisect

### CODE HERE

def ans(A, queries):
    ret = []
    A.sort()

    TOTAL = sum(A)

    def score(idx, x, y):
        if A[idx] >= x:
            cost_to_attack = 0
        else:
            cost_to_attack = x - A[idx]

        rest = TOTAL - A[idx]
        if rest > y:
            cost_to_defend = 0
        else:
            cost_to_defend = y - rest

        return cost_to_attack + cost_to_defend

    for x, y in queries:
        indices = []
        i = bisect.bisect_left(A, x)
        j = bisect.bisect_right(A, x)
        indices += [i-1, i, i+1, j-1, j, j+1]
        indices = [i for i in indices if 0 <= i < len(A)]
        indices = list(set(indices))
        indices = indices
        ret += [min(score(i, x, y) for i in indices)]

    return ret

if True:
    import random
    N = 2*10**5
    A = [random.randint(1, 10**12) for _ in range(N)]
    queries = [(random.randint(1, 10**12), random.randint(1, 10**12)) for _ in range(N)]
    ans(A, queries)
else:
    N = read_int()
    A = read_int_list()
    queries = []
    for _ in range(read_int()):
        x, y = read_int_tuple()
        queries += [(x, y)]
    print('\n'.join(map(str,ans(A, queries))))