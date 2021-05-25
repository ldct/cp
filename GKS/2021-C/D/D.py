#!/usr/bin/env python3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from functools import partial, lru_cache

class Infix(object):
    def __init__(self, func):
        self.func = func
    def __or__(self, other):
        return self.func(other)
    def __ror__(self, other):
        return Infix(partial(self.func, other))
    def __call__(self, v1, v2):
        return self.func(v1, v2)

import random

@Infix
@lru_cache(None)
def op(x, y):
    return random.randint(0, 2**64-1)

def ans(cases):

    ret = []

    low_of = dict()

    last = 1

    for case in cases:
        c = case.replace("#", " |op| ")
        c = eval(c, globals(), locals())

        if c not in low_of:
            low_of[c] = last
            last += 1
        ret += [low_of[c]]

    return ' '.join(map(str, ret))

for t in range(read_int()):
    cases = []
    for _ in range(read_int()):
        cases += [input()]
    print("Case #" + str(t+1) + ": " + str(ans(cases)))
