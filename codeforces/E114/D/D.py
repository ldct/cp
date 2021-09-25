#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from heapq import *

def neighbours(tup):
    ret = []
    for i in range(len(tup)):
        if tup[i] > 0:
            c = list(tup)
            c[i] -= 1
            ret += [c]
    return ret

def score2(elems, tup):
    ret = 0
    for idx, elem in zip(tup, elems):
        ret -= elem[idx]
    return ret

def combinations(elems):

    def score(tup):
        return score2(elems, tup)

    start = tuple(len(x)-1 for x in elems)
    yield start

    candidates = []

    for tup in neighbours(start):
        heappush(candidates, [score(tup)] + tup)

    yielded = set()
    yielded.add(start)

    while len(candidates):
        tup = heappop(candidates)[1:]
        yield tup
        yielded.add(tuple(tup))

        for n in neighbours(tup):
            if tuple(n) in yielded: continue
            heappush(candidates, [score(n)] + n)

### CODE HERE

def ans(equipments, banned):
    for tup in (list(combinations(equipments))):
        if tuple(tup) not in banned:
            return tup

    ### NON-PQ solution here
    start = tuple(len(x)-1 for x in equipments)
    if start not in banned:
        return start
    candidates = []
    for tup in banned:
        for n in neighbours(tup):
            if tuple(n) not in banned:
                candidates += [(-score2(equipments, n), n)]
    return max(candidates)[1]

if False:
    r = list(range(100))
    for i, c in enumerate(combinations([r, r, r, r, r])):
        if i == 10**5:
            print(c)
            break
else:

    equipments = []
    banned = set()

    for _ in range(read_int()):
        equipments += [read_int_list()[1:]]
    for _ in range(read_int()):
        b = read_int_list()
        b = [i-1 for i in b]
        banned.add(tuple(b))
    r = ans(equipments, banned)
    r = [x+1 for x in r]
    print(*r)