#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

H, W, M = input().split()
H = int(H)
W = int(W)
M = int(M)

x_score = [0]*300009
y_score = [0]*300009

elems = set()

for _ in range(M):
    h, w = input().split()
    h = int(h)
    w = int(w)

    x_score[h] += 1
    y_score[w] += 1

    elems.add((h, w))

best_x_score = max(x_score)
best_y_score = max(y_score)

best_x = []
best_y = []

for i in range(len(x_score)):
    if x_score[i] == best_x_score:
        best_x += [i]
    
for i in range(len(y_score)):
    if y_score[i] == best_y_score:
        best_y += [i]

import sys

if len(best_x)*len(best_y) > M+10:
    print(best_x_score + best_y_score)
    sys.exit(0)

for x in best_x:
    for y in best_y:
        if (x, y) not in elems:
            print(best_x_score + best_y_score)
            sys.exit(0)

print(best_x_score + best_y_score - 1)
