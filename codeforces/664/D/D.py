#!/usr/bin/env pypy3

import math

n,d,m = input().split()
n = int(n)
d = int(d)
m = int(m)
A = list(map(int, input().split()))

rude = []
polite = []

for a in A:
    if a > m:
        rude += [a]
    else:
        polite += [a]

rude = sorted(rude)[::-1]
polite = sorted(polite)[::-1]

rude_prefix = [0]
for r in rude:
    rude_prefix += [rude_prefix[-1] + r]
for _ in range(n):
    rude_prefix += [rude_prefix[-1]]

polite_prefix = [0]
for p in polite:
    polite_prefix += [polite_prefix[-1] + p]
for _ in range(n):
    polite_prefix += [polite_prefix[-1]]


ans = float("-inf")

for np in range(len(polite)+1):
    polite_score = polite_prefix[np]
    rude_cells = n - np
    num_rude = math.ceil(rude_cells / (d+1))
    rude_score = rude_prefix[num_rude]
    ans = max(ans, polite_score + rude_score)

print(ans)
