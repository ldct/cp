#!/usr/bin/env python3

from collections import defaultdict

def score(D, c, s, v):

    ret = []
    last = defaultdict(int)

    satisfaction = 0
    for d in range(1, D+1):
        satisfaction += s[(d, v[d])]
        last[v[d]] = d
        for i in range(1,27):
            satisfaction -= c[i]*(d - last[i])
        ret += [satisfaction]

    return '\n'.join(map(str, ret))

D = int(input())
c = input().split(' ')
c = list(map(int, c))
c = [float("inf")] + c
s = dict()
v = [float("inf")]
for i in range(D):
    row = input().split(' ')
    for j, e in enumerate(row):
        e = int(e)
        s[(i+1, j+1)] = e
for _ in range(D):
    v += [int(input())]

print(score(D, c, s, v))