#!/usr/bin/env python3

import array

with open('capture.in', 'r') as f:
    N, R, C, A, B = map(int, f.readline().split(" "))
    net_pos = []
    for n in range(N):
        r,c = map(int, f.readline().split(" "))
        net_pos.append((r,c))

min_dist_matrix = []

for r in range(R):
    row = []
    for c in range(C):
        row += [min([abs(rp-r) + abs(cp - c) for (rp, cp) in net_pos])]
    min_dist_matrix += [row]

# find smallest window
out = []
for r in range(R-A + 1):
    for c in range(C-B + 1):
        window = []
        for subr in range(r, r+A):
            window.extend(min_dist_matrix[subr][c:c+B])
        out.append(min(window))

with open('capture.out', 'w') as g:
    print(max(out), file=g)