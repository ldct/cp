#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(N, L, R, S):

    old_S = S
    box = []

    n = R - L + 1
    for i in range(n):
        box += [i+1]

    if sum(box) > S: return [-1]

    j = len(box)-1
    S -= sum(box)
    while True:
        if j == -1: return [-1]
        if S == 0: break
        if box[j] + 1 <= N and (box[j] + 1) not in box:
            box[j] += 1
            S -= 1
        else:
            j -= 1

    rest = [1]
    while rest[-1] != N: rest += [rest[-1] + 1]

    rest = [r for r in rest if r not in box]

    return rest[0:L-1] + box + rest[L-1:]

for _ in range(read_int()):
    N, L, R, S = read_int_tuple()
    print(*ans(N, L, R, S))