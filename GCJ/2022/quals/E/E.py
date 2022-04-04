#!/usr/bin/env pypy3

from sys import stdin, stdout

def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import defaultdict

import random

def fprint(*args):
	print(*args, flush=True)

T = read_int()
for _ in range(T):
    N, K = read_int_tuple()

    score = 0

    R, P = read_int_tuple()
    fprint(f"T {random.randint(1, N)}")

    SMALL_SAMPLE = (K-1) // 2
    BIG_SAMPLE = (K-1) // 2

    for i in range(SMALL_SAMPLE):
        R, P = read_int_tuple()
        score += P / SMALL_SAMPLE
        fprint(f"T {random.randint(1, N)}")

    degree = defaultdict(int)
    for i in range(BIG_SAMPLE):
        R, P = read_int_tuple()
        if i > 5:
            degree[R] = P
        fprint(f"W")

    for u in degree:
        score += degree[u] / N

    R, P = read_int_tuple()
    guess = int(N*score/2)
    fprint(f"E {guess}")
