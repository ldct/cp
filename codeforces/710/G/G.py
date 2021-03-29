#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import defaultdict
from itertools import product

### CODE HERE

ALPHABET = "abcdefghijklmnopqrstuvwxyz"[::-1]

def ans_slow(S):
    indexes = defaultdict(set)

    for i, c in enumerate(S):
        indexes[c].add(i)

    keys = []
    values = []

    for c in ALPHABET:
        if len(indexes[c]) > 0:
            keys += [c]
            values += [indexes[c]]

    candidates = []

    for ic in product(*values):
        candidate = sorted(list(zip(ic, keys)))
        candidate = [c for _, c in candidate]
        candidates += [''.join(candidate)]

    return max(candidates)

def ok(s1, s2):
    for c in set(s1):
        if c not in s2: return False
    return True

def ans(S):

    def index(S, i, c):
        for j in range(i, len(S)):
            if S[j] == c: return j
        return None

    assigned = []

    while len(S):
        for c in ALPHABET:
            if c in assigned: continue
            i = index(S, 0, c)
            if i is None:
                continue
            if ok(S[0:i], S[i+1:]):
                assigned += [c]
                S = S[i:].replace(c, '')
                break
                # print("assigning", c, "S=", S)

    assigned = ''.join(assigned)

    return assigned

if False:
    import sys, random
    for _ in range(10000):
        tc = ''.join(random.choice('abcde') for _ in range(10))
        if ans(tc) != ans_slow(tc):
            print(tc, ans(tc), ans_slow(tc))
            sys.exit(0)
    sys.exit(0)

for _ in range(read_int()):
    S = input()
    print(ans(S))