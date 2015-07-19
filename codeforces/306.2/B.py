#!/usr/bin/env python3

from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

N, L, R, X = map(int, input().split(' '))
C = map(int, input().split(' '))

def is_ok(c):
    if len(c) < 2:
        return False
    if not (L <= sum(c) <= R):
        return False
    if max(c) - min(c) < X:
        return False
    return True

print(sum([1 for c in powerset(C) if is_ok(c)]))