#!/usr/bin/env python2

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

def ans(L):
    ret = 0
    for i in range(len(L)-1):
        Lj = min(L[i:])
        j = L.index(Lj)
        L[i:j+1] = L[i:j+1][::-1]
        ret += j-i+1
    return ret

T = int(input())
for t in range(T):
    input()
    L = read_int_list()
    print("Case #" + str(t+1) + ": " + str(ans(L)))
