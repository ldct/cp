#!/usr/bin/env pypy3

from __future__ import division, print_function

import itertools
import sys

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

MAX = 10**6+10
roaring = set()

def ans_exact(S, bb):
    ret = [bb]
    while len(ret) < 2 or (int(''.join(map(str, ret)), 10) <= S):
        ret += [ret[-1] + 1]
    # print("ans_exact", S, bb, "=", ret)

    return ''.join(map(str, ret))

def ans(S):
    candidates = []
    for bb in [10**e for e in range(24)]:
        candidates += [ans_exact(S, bb)]
    for pl in range(1, len(str(S))+1):
        pp = int(str(S)[0:pl])
        for p in range(pp, pp+1000):
            candidates += [ans_exact(S, p)]
    candidates = map(int, candidates)
    return min(candidates)


for start in range(1, MAX):
    for cl in range(2,8):
        candidate = [start]
        while len(candidate) != cl:
            candidate += [candidate[-1] + 1]

        candidate = ''.join(map(str, candidate))

        if int(candidate) > 1234567: continue

        roaring.add(int(candidate))



def ans_slow(Y):
    for i in range(Y+1, 2*MAX):
        if i in roaring:
            return i

for i in range(1, 10000000000):
    if not (ans(i) == ans_slow(i)):
        print(i, ans(i), ans_slow(i))
sys.exit(0)

T = int(input())
for t in range(T):
    Y = read_int()
    print("Case #" + str(t+1) + ": " + str(ans(Y)))
