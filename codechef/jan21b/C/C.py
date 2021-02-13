#!/usr/bin/env pypy3

from sys import stdin, stdout

def input():
    return stdin.readline().strip()

def read_line():
    return list(map(int, input().split()))

def read_int():
    return int(input())

### CODE HERE

def ans(lines):
    if len(lines) == 1:
        [M] = lines
        M = M[1:]
        neg = 0
        pos = 0
        for m in M:
            if m > 0: pos += 1
            elif m < 0: neg += 1
            else: assert(False)
        return pos*neg
    else:
        return len(lines)

for _ in range(read_int()):
    N = read_int()
    lines = []
    for _ in range(N):
        lines += [read_line()]

    print(ans(lines))
