#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def make_fill(N, M, val):
    ret = []
    for _ in range(N):
        ret += [[val]*M]
    return ret

N, A, B = read_int_tuple()
P, Q, R, S = read_int_tuple()

A -= 1
B -= 1
P -= 1
Q -= 1
R -= 1
S -= 1

ret = make_fill(Q - P + 1, S - R + 1, '.')

for i in range(Q-P+1):
    for j in range(S-R+1):
        x = P+i
        y = R+j
        dx = x - A
        dy = y - B
        if abs(dx) == abs(dy):
            ret[i][j] = '#'

p = []
for row in ret:
    p += [''.join(row)]
print('\n'.join(p))
