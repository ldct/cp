#!/usr/bin/env pypy

from __future__ import division, print_function

import itertools, sys, math

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

MODULUS = 10**9+7

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import product

def ans(R, C, K, r1, c1, r2, c2):
    if K != 1: return -1

    ret = 0

    h = r2 - r1 + 1
    w = c2 - c1 + 1

    ret += (w+1)*h + (h+1)*w

    cd_left = c1 - 1
    cd_right = C - c2
    cd_up = r1 - 1
    cd_down = R - r2

    ret += min(cd_left, cd_right, cd_up, cd_down)

    if r1 == 1: ret -= w
    if r2 == R: ret -= w
    if c1 == 1: ret -= h
    if c2 == C: ret -= h

    return ret

for t in range(read_int()):
    R, C, K = read_int_tuple()
    r1, c1, r2, c2 = read_int_tuple()
    print("Case #" + str(t+1) + ": " + str(ans(R, C, K, r1, c1, r2, c2)))
