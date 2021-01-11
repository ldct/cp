#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from itertools import product
from random import shuffle
from heapq import *
from collections import defaultdict

def greedy(cards, showing):
    showing = set(showing)

    for (a, b) in cards:
        if a not in showing:
            showing.add(a)
            continue
        if b not in showing:
            showing.add(b)
            continue

    return len(showing)

def ans(cards):

    cards = [tuple(sorted(card)) for card in cards]

    showing = set()

    seen = set()
    for card in cards:
        if card in seen:
            (a, b) = card
            showing.add(a)
            showing.add(b)
        else:
            seen.add(card)

    while True:
        redo_loop = False

        for (a, b) in cards:
            if a == b and a not in showing:
                showing.add(a)
                redo_loop = True

        for (a, b) in cards:
            if a in showing and b not in showing:
                showing.add(b)
                redo_loop = True
            if a not in showing and b in showing:
                showing.add(a)
                redo_loop = True


        if not redo_loop:
            break

    deg = defaultdict(int)
    neighbours = defaultdict(set)

    for (a, b) in cards:
        deg[a] += 1
        deg[b] += 1
        neighbours[a].add(b)
        neighbours[b].add(a)

    pq = []
    for k in deg:
        pq += [(deg[k], k)]

    heapify(pq)

    while len(pq):
        (d, u) = heappop(pq)
        if deg[u] != d: continue
        if d == 1:
            showing.add(u)
            for v in neighbours[u]:
                neighbours[v].remove(u)
                deg[v] -= 1
                heappush(pq, (deg[v], v))


    for k in deg:
        if deg[k] >= 2:
            showing.add(k)

    return len(showing)

def ans_slow(cards):
    ret = -1
    for p in product(*cards):
        ret = max(ret, len(set(p)))
    return ret

# tc = [(1, 6), (1, 8), (7, 1), (7, 6), (8, 7)]
# print(ans_slow(tc), ans(tc))

# import random
# for _ in range(100000000):
#     N = 6
#     tc = [(random.randint(1, 10), random.randint(1, 10)) for _ in range(N)]
#     if ans(tc) != ans_slow(tc):
#         print(tc)
#         break

cards = []
for _ in range(read_int()):
    cards += [read_int_tuple()]

print(ans(cards))