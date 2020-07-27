#!/usr/bin/env python3

with open('nfc.in', 'r') as f:
    lines = f.read().split('\n')

NK = lines[0].split(' ')
N = NK[0]
K = NK[1]
N = int(N)
K = int(K)

D = lines[1:]
D = [int(d) for d in D if len(d)]

assert(N == len(D))

index_of = dict()

for i, d in enumerate(D):
    if d not in index_of:
        index_of[d] = i

min_sum = float("inf")

for i, d in enumerate(D):
    target = K - d
    if target not in index_of: continue

    j = index_of[target]

    if i+j < min_sum:
        min_sum = i+j

valids = []
for i, d in enumerate(D):
    target = K - d
    if target not in index_of: continue

    j = index_of[target]

    if i+j == min_sum:
        valids += [(i, j)]

valids = sorted(valids)

with open('nfc.out', 'w') as g:
    i, j = valids[0]
    [i, j] = sorted([i, j])
    print(i+1, j+1, file=g)
