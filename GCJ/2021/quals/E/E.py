#!/usr/bin/env python2

from __future__ import division, print_function

import itertools
import sys
from math import exp

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

T = int(input())
P = int(input())
for t in range(T):
    q_correct_count = [0]*10000
    scores = []
    for _ in range(100):
        score = list(map(int, input()))
        for i, s in enumerate(score):
            q_correct_count[i] += s
        scores += [score]
    q_correct_count = [(e, i) for i, e in enumerate(q_correct_count)]
    q_correct_count = sorted(q_correct_count)
    q_correct_count = [i for _, i in q_correct_count]
    scores = [[score[q] for q in q_correct_count] for score in scores]

    oddities = []

    for i, score in enumerate(scores):
        oddity = 0
        flip = sum(score) / 10000
        for j in range(len(score)):
            pos = j / 10000 - flip
            p = 1/(1 + exp(-6*pos))
            if score[j] == 0:
                oddity += p
            else:
                oddity += 1-p

        oddities += [(oddity, i, sum(score[0:100]))]

    oddities = sorted(oddities)[::-1]
    # for o in oddities:
    #     print(o)
    guess = oddities[0][1] + 1

    print("Case #" + str(t+1) + ": " + str(guess))
