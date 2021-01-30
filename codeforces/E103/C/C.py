#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def dp(block):
    if len(block) <= 1: return
    print(block)

    memo = [-1]*len(block)
    memo[-2] = block[-1]+2

    # block[0] = (block[0], 0)
    block[-1] = (block[-1], 0)

    for i in range(len(block)-3, -1, -1):
        memo[i] = max(
            2+sum(block[i+1]),
            2+block[i+1][1] + memo[i+1]
        )

    for i in range(len(block)-1):
        memo[i] += 0
    print(memo)

def ans(chains):
    blocks = []
    curr_block = []

    C = []
    N = []

    for c, a, b in chains:
        C += [c-1]

    for i, (c, a, b) in enumerate(chains):
        if i > 0:
            N += [b - a]

    N += [C[-1]]

    chains = list(zip(C, N))

    return chains

for _ in range(read_int()):
    N = read_int()
    C = read_int_list()
    A = read_int_list()
    B = read_int_list()

    chains = []
    for i in range(N):
        a, b = A[i], B[i]
        [a, b] = sorted([a, b])
        chains += [(C[i], a, b)]
    print(ans(chains))