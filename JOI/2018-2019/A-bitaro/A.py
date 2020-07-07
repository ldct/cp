#!/usr/bin/env pypy3

import array

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

H, W = input().split(' ')

H = int(H)
W = int(W)

S = []

for _ in range(H):
    S += [input()[::-1]]

S = S[::-1]

# inject test case

if False:
    import random
    H = 3000
    W = 3000
    S = []
    for _ in range(H):
        row = [0]*W
        S += [row]
    for x in range(H):
        for y in range(W):
            S[x][y] = random.choice("JOI")

    exit(0)
# end inject test case

O_count = []
for _ in range(H):
    row = array.array('i', [0]*W)
    O_count += [row]

I_count = []
for _ in range(H):
    row = array.array('i', [0]*W)
    I_count += [row]

for y in range(W):
    count = 0
    for x in range(H):
        if S[x][y] == 'I': count += 1
        I_count[x][y] = count

for x in range(H):
    count = 0
    for y in range(W):
        if S[x][y] == 'O': count += 1
        O_count[x][y] = count

# print('\n'.join(S))
# print('\n'.join(' '.join(str(r) for r in row) for row in O_count))
# print(I_count)

ans = 0
for x in range(H):
    for y in range(W):
        if S[x][y] == 'J':
            ans += O_count[x][y] * I_count[x][y]

print(ans)