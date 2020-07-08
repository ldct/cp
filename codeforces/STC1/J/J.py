#!/usr/bin/env pypy3

""" Python 3 compatibility tools. """
from __future__ import division, print_function

import itertools
import sys

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

import os
import sys
from atexit import register
from io import BytesIO

sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))

input = lambda: sys.stdin.readline().rstrip('\r\n')

def largest_idx(s1, s2):
    for i in range(len(s1)):
        if i == len(s2) or s1[i] != s2[i]: return i
    assert(False)

def largest_deletion(s1, s2):
    i = largest_idx(s1, s2)
    s1 = list(s1)
    del s1[i]
    s1 = ''.join(s1)
    if s1 == s2: return i
    return None

def smallest_idx(s1, s2):
    return len(s2) - largest_idx(s1[::-1], s2[::-1])

def smallest_deletion(s1, s2):
    i = smallest_idx(s1, s2)
    s1 = list(s1)
    del s1[i]
    s1 = ''.join(s1)
    if s1 == s2: return i
    return None

# test injection
if True:    
    s1 = input()
    s2 = input()
else:
    s2 = "a"*10**6
    s1 = s2 + "a"
    print(s1)
    print(s2)

    exit(0)
    
i = smallest_deletion(s1, s2)
j = largest_deletion(s1, s2)

if i is None or j is None:
    assert(i is None and j is None)
    print(0)
else:
    print(j-i+1)
    print(*list(range(i+1,j+2)))