#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

R = []
G = []
B = []

for _ in range(2*read_int()):
    a, c = input().split()
    a = int(a)
    if c == 'R': R += [a]
    if c == 'G': G += [a]
    if c == 'B': B += [a]

groups = []
if len(R) % 2 == 1: groups += ['R']
if len(G) % 2 == 1: groups += ['G']
if len(B) % 2 == 1: groups += ['B']

BIG_MAP = {'R': R, 'G': G, 'B': B}

others = set('RGB') - set(groups)
assert(len(groups) % 2 == 0)

def closest(g1, g2):
    g1 = [(a, 'R') for a in g1]
    g2 = [(a, 'G') for a in g2]
    points = sorted(g1 + g2)

    candidates = []
    for i in range(len(points) - 1):
        p1 = points[i]
        p2 = points[i+1]

        if p1[1] == p2[1]: continue

        candidates += [(abs(p1[0] - p2[0]), p1[0], p2[0])]

    if len(candidates) == 0: return float("inf")
    return min(candidates)[0]

if len(groups) == 0:
    print(0)
elif len(groups) == 2:
    [g1, g2] = groups
    g1 = BIG_MAP[g1]
    g2 = BIG_MAP[g2]


    choice1 = closest(g1, g2)

    [other] = list(others)
    g3 = BIG_MAP[other]

    choice2 = closest(g3, g1) + closest(g3, g2)

    print(min(choice1, choice2))

else:
    assert(False)
