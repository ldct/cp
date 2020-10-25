#!/usr/bin/env pypy3

from math import factorial
from itertools import chain, combinations, permutations

def subsets(iterable, low=0, high=None):
    "subsets([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    if high is None:
        high = len(s)
    return chain.from_iterable(combinations(s, r) for r in range(low, high+1))

def normalize(p):
    ret = []
    for i in range(len(p)):
        if p[i] == 0: break

    for k in range(len(p)):
        ret += [p[(i+k) % len(p)]]

    # return tuple(ret)

    r1 = [ret[0]] + ret[1:]
    r2 = [ret[0]] + ret[1:][::-1]

    return max(
        tuple(r1),
        tuple(r2)
    )

def cp(n):
    ret = set()
    for p in permutations(list(range(n))):
        ret.add(normalize(p))
    return len(ret)

for i in range(1, 10):
    print(i, cp(i))

def sub(a, b):
    ret = []
    for x in a:
        if x not in b:
            ret += [x]
    return tuple(ret)

def ans_fast(n):
    return factorial(n+1) // (n//2 + 1)

def ans(n):
    persons = list(range(n))
    ret = set()
    for s in subsets(persons, n//2, n//2):
        if 0 not in s: continue

        s1 = s
        s2 = sub(persons, s)

        for p1 in permutations(s1):
            for p2 in permutations(s2):
                ret.add((normalize(p1), normalize(p2)))

    return len(ret) // (n // 2)

# for n in range(2, 16, 2):
#     print(n, ans(n), ans_fast(n-2))

n = int(input())
print(ans_fast(n-2))