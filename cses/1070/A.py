#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(N):
    if N == 1:
        return [1]

    if N <= 3:
        return ["NO SOLUTION"]

    core = [3, 1, 4, 2]

    odds = []
    evens = []

    for i in range(1, N+1):
        if i in core: continue
        (evens if i % 2 == 0 else odds).append(i)

    return evens + core + odds

N = read_int()

print(*ans(N))