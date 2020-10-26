#!/usr/bin/env pypy3

from sys import stdin, stdout

def input():
    return stdin.readline().strip()

def southmost(spans, start):
    ret = -1

    for span in spans:
        eligible = [s for s in span if s >= start]
        if len(eligible) == 0:
            return None
        ret = max(ret, min(eligible))

    return ret

def northmost(spans, start):
    ret = float("inf")

    for span in spans:
        eligible = [s for s in span if s <= start]
        if len(eligible) == 0:
            return None
        ret = min(ret, max(eligible))

    return ret


def gap_fast(span):
    ret = float("inf")

    for start in span[0]:
        sm = southmost(span, start)
        if sm is not None:
            ret = min(ret, sm - start)

    for end in span[0]:
        nm = northmost(span, end)
        if nm is not None:
            ret = min(ret, end - nm)

    return ret

def gap_slow(span):
    indices = set()
    for s in span:
        for x in s:
            indices.add(x)


    ret = float("inf")
    for start in indices:
        sm = southmost(span, start)
        if sm is not None:
            ret = min(ret, sm - start)
    return ret

def ans(frets, B):
    span = [[b - f for f in frets if b - f >= 0] for b in B]
    indices = set()
    for s in span:
        for x in s:
            indices.add(x)

    return gap_fast(span)


def test_case():
    import random
    return [[random.randint(0, 5) for _ in range(2)] for _ in range(3)]

# for _ in range(10000):
#     tc = test_case()
#     if gap_fast(tc) != gap_slow(tc):
#         print(tc)
#         break

tc = [[4, 1], [0, 0], [2, 4]]
print(gap_fast(tc))

# frets = list(map(int, input().split()))
# input()
# B = list(map(int, input().split()))
# print(ans(frets, B))