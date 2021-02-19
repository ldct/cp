#!/usr/bin/env pypy3

from sys import stdin, stdout

### CODE HERE

from functools import lru_cache

def fprint(*args):
	print(*args, flush=True)

@lru_cache(None)
def query(a, b):
    assert(a <= b)
    if a == b: return a
    fprint(f"? {a} {b}")
    return int(input())

N = int(input())

mid = query(1, N)

to_right = None
if mid == N:
    to_right = False
elif mid == 1:
    to_right = True
else:
    left = query(1, mid)
    right = query(mid, N)
    assert(left == mid or right == mid)
    to_right = (right == mid)

def doit():
    # print("doing it", to_right)
    if to_right:
        def contains_ans(r):
            if mid == r: return False
            return query(mid, r) == mid

        i = mid
        j = N

        while j - i > 2:
            assert(not contains_ans(i))
            assert(contains_ans(j))

            k = (i + j) // 2
            if contains_ans(k):
                j = k
            else:
                i = k

        for t in range(i, i+5):
            if contains_ans(t):
                return t

        assert(False)

    else:
        def contains_ans(l):
            if l == mid: return False
            return query(l, mid) == mid
        i = 1
        j = mid

        while j - i > 2:
            assert(contains_ans(i))
            assert(not contains_ans(j))

            k = (i + j) // 2
            if contains_ans(k):
                i = k
            else:
                j = k

        for t in range(j, j-5, -1):
            if contains_ans(t):
                return t

        assert(False)

fprint("!", doit())