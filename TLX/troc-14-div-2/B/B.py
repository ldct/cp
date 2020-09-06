#!/usr/bin/env pypy3

N, M = input().split()
N = int(N)
M = int(M)

ret = []
for _ in range(N):
    row = ['?']*M
    ret += [row]

for i in range(N):
    for j in range(M):
        c = 'W'
        if j % 2 == 1:
            c = 'B'
        ret[i][j] = c

for row in ret:
    print(''.join(row))
