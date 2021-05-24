#!/usr/bin/env pypy

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

import random

def ans(W, E):
    if E == 0: return 'R'*22 +'S'*(60-22)
    if E == W//10: return 'R'*22 +'S'*(60-22)
    if W == E: return 'RSP'*20
    if E == W//2: return 'RSP'*20

T = read_int()
X = read_int()
for t in range(T):
    W, E = read_int_tuple()
    print("Case #" + str(t+1) + ": " + str(ans(W, E)))
