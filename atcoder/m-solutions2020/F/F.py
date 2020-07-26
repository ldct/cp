#!/usr/bin/env pypy3

from collections import defaultdict

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

forward_diag = defaultdict(list)
backward_diag = defaultdict(list)
updown = defaultdict(list)
leftright = defaultdict(list)

elems = []
N = int(input())
for _ in range(N):
    x, y, U = input().split(' ')
    x = int(x)
    y = int(y)
    U
    elems += [(x, y, U)]

N = len(elems)


for x, y, U in elems:
    forward_diag[x-y] += [(x, U)]
    backward_diag[x+y] += [(x, U)]
    updown[x] += [(y, U)]
    leftright[y] += [(x, U)]

min_collisions = float("inf")

def search(lst, A, B):
    ret = float("inf")
    lst = sorted([(a, d) for (a, d) in lst])
    i = 0
    while i < len(lst):
        while i < len(lst) and lst[i][1] != A:
            i += 1
        j = i
        while j < len(lst) and lst[j][1] != B:
            j += 1
        if i < len(lst) and j < len(lst):
            ret = min(ret, lst[j][0]-lst[i][0])
        i += 1
    return ret

for lst in updown.values():
    min_collisions = min(min_collisions, 5*search(lst, 'U', 'D'))
for lst in leftright.values():
    min_collisions = min(min_collisions, 5*search(lst, 'R', 'L'))
for lst in forward_diag.values():
    min_collisions = min(min_collisions, 10*search(lst, 'U', 'L'))
    min_collisions = min(min_collisions, 10*search(lst, 'R', 'D'))
for lst in backward_diag.values():
    min_collisions = min(min_collisions, 10*search(lst, 'R', 'U'))
    min_collisions = min(min_collisions, 10*search(lst, 'D', 'L'))

if min_collisions == float("inf"):
    print("SAFE")
else:
    print(min_collisions)
