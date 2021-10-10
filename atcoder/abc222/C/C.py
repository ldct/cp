#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

N, M = read_int_list()
A = []
for _ in range(2*N):
    A += [input()]

rankings = [[0, i] for i in range(2*N)]

def bump(idx):
    rankings[idx][0] += 1

def win(a, b):
    return a + b in ["GC", "CP", "PG"]

def match(a, b, match_idx):
    a_play = A[rankings[a][1]][match_idx]
    b_play = A[rankings[b][1]][match_idx]

    if win(a_play, b_play):
        bump(a)
    elif win(b_play, a_play):
        bump(b)

for match_idx in range(M):
    for i in range(N):
        match(2*i, 2*i+1, match_idx)
    rankings.sort(key=lambda p: (-p[0], p[1]))

for _, i in rankings:
    print(i+1)
