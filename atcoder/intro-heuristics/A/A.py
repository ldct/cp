#!/usr/bin/env python3

from collections import defaultdict
from copy import deepcopy

def greedy(D, c, s):

    ret = []
    last = defaultdict(int)

    for d in range(1, D+1):

        last = defaultdict(int)
        scores = dict()


        for choice in range(1,27):
            _last = deepcopy(last)  
            satisfaction = s[(d, choice)]
            _last[choice] = d
            for i in range(1,27):
                satisfaction -= c[i]*(d - _last[i])

            scores[choice] = satisfaction

        choice = max(scores, key=scores.get)
        ret += [choice]
        last[choice] = d

    return '\n'.join(map(str, ret))

D = int(input())
c = input().split(' ')
c = list(map(int, c))
c = [float("inf")] + c
s = dict()
for i in range(D):
    row = input().split(' ')
    for j, e in enumerate(row):
        e = int(e)
        s[(i+1, j+1)] = e

print(greedy(D, c, s))