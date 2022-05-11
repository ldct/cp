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

# 240 -> 247 -> 276
def ans(W, E):
    if E == 0:
        return 'SPPPPPPPPPRRRRRRRRRRRRRRRRRRRRRRRRRRRSSSSSSSSSSSSSSSSSSSSSSS' # 237
        return 'R'*22 +'S'*(60-22) # 189
        return 'R'*30 +'S'*(60-30) # 178

    if E == W//2:
        return 'SPPRRRRSSSSSSSSPPPPPPPPPPPPPPPPRRRRRRRRRRRRRRRRRRRSSSSSSSSSS' # 278
        return 'RSP'*20 # 264

    if W == E:
        return 'RSP'*20 # 346

    if E == W//10:
        return 'SPPPPRRRRRRRRRRRRRRRSSSSSSSSSSSSSSSSSSSSSSSSSPPPPPPPPPPPPPPP' # 242
        return 'SPPPPPPPPPRRRRRRRRRRRRRRRRRRRRRRRRRRRSSSSSSSSSSSSSSSSSSSSSSS' # 242
        return 'R'*22 +'S'*(60-22) # 189

T = read_int()
X = read_int()
for t in range(T):
    W, E = read_int_tuple()
    print("Case #" + str(t+1) + ": " + str(ans(W, E)))
