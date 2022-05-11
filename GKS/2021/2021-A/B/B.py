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

def num(a, b):
    for _ in range(5):
        a = min(a, 2*b)
        b = min(b, a // 2)

    if b < 2: return 0

    return b - 1

    return a,b

def ans(H, W, S):

    BAD_CELL = 0

    i_min = []
    for _ in range(H): i_min += [[-1]*(W)]

    for j in range(W):
        if S[0][j] == BAD_CELL:
            i_min[0][j] = 0
        else:
            i_min[0][j] = -1
        for i in range(1,H):
            if S[i][j] == BAD_CELL:
                i_min[i][j] = i
            else:
                i_min[i][j] = i_min[i-1][j]

    i_max = []
    for _ in range(H): i_max += [[-1]*(W)]

    for j in range(W):
        if S[H-1][j] == BAD_CELL:
            i_max[H-1][j] = H-1
        else:
            i_max[H-1][j] = H
        for i in range(H-2,-1,-1):
            if S[i][j] == BAD_CELL:
                i_max[i][j] = i
            else:
                i_max[i][j] = i_max[i+1][j]

    j_min = []
    for _ in range(H): j_min += [[-1]*(W)]

    for i in range(H):
        if S[i][0] == BAD_CELL:
            j_min[i][0] = 0
        else:
            j_min[i][0] = -1
        for j in range(1,W):
            if S[i][j] == BAD_CELL:
                j_min[i][j] = j
            else:
                j_min[i][j] = j_min[i][j-1]

    j_max = []
    for _ in range(H): j_max += [[-1]*(W)]

    for i in range(H):
        if S[i][W-1] == BAD_CELL:
            j_max[i][W-1] = W-1
        else:
            j_max[i][W-1] = W
        for j in range(W-2,-1,-1):
            if S[i][j] == BAD_CELL:
                j_max[i][j] = j
            else:
                j_max[i][j] = j_max[i][j+1]

    ret = 0

    for i in range(H):
        for j in range(W):
            right = j_max[i][j] - j
            up = i - i_min[i][j]
            left = j - j_min[i][j]
            down = i_max[i][j] - i

            for (a, b) in [(right, up), (right, down), (down, left), (left, up)]:
                if a < 2 or b < 2: continue

                ret += num(a,b) + num(b,a)


                # print((a, b), num(a, b), num(b, a))

    return ret

T = int(input())
for t in range(T):
    R, C = input().split()
    R = int(R)
    C = int(C)
    matrix = []
    for _ in range(R):
        matrix += [list(map(int, input().split()))]
    print("Case #" + str(t+1) + ": " + str(ans(R,C,matrix)))
