#!/usr/bin/env pypy3

from __future__ import division, print_function

import itertools
import sys
import array
from collections import Counter, defaultdict
import random

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import product

def match(A, B):
    ret = 0
    for a, b in zip(A, B):
        if a == b: ret += 1
    return ret

def consistent(p, data):
    for A, S in data:
        if match(p, A) != S: return False
    return True

def ans_slow(data):
    N = len(data[0][0])

    corrects = []
    for p in product('TF', repeat=N):
        if not consistent(p, data):
            continue
        corrects += [p]

    ret = 0

    for p in product('TF', repeat=N):
        score = 0
        for c in corrects:
            score += match(p, c)
        ret = max(ret, score)

    if ret % len(corrects) == 0:
        return ret // len(corrects)
    return ret / len(corrects)

def inv(S):
    ret = []
    for s in S:
        if s == 'T': ret += ['F']
        if s == 'F': ret += ['T']
    return ''.join(ret)

def ans(data):
    N = len(data[0][0])

    D = dict()

    for A, S in data:
        D[S] = ''.join(A)
        D[N-S] = inv(A)

    m = max(D.keys())

    return D[m] + ' ' + str(m) + '/1'

if False:
    for _ in range(100000000):
        N = 5
        A = ''.join(random.choice('TF') for _ in range(N))
        B = ''.join(random.choice('TF') for _ in range(N))

        data = [
            (A, random.randint(0, N)),
            (B, random.randint(0, N))
        ]

        corrects = []
        for p in product('TF', repeat=N):
            if not consistent(p, data):
                continue
            corrects += [p]
        if len(corrects) == 0: continue

        if ans(data) != ans_slow(data):
            print(data, ans(data), ans_slow(data))


T = read_int()
for t in range(T):
    N, Q = read_int_tuple()

    data = []
    for _ in range(N):
        A, S = input().split()
        S = int(S)
        data += [(A, S)]

    print("Case #" + str(t+1) + ": " + str(ans(data)))
