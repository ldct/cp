#!/usr/bin/env pypy3

from sys import stdin, stdout

def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import defaultdict
from functools import lru_cache

import random

def fprint(*args):
	print(*args, flush=True)

@lru_cache(None)
def A_of(N):
    ret = []

    i = 0
    while True:
        if len(ret) >= N or 2**i > 10**9: break
        ret += [2**i]
        i += 1

    sr = set(ret)

    for i in range(1, 10**9):
        if len(ret) == N: return ret
        if i not in sr:
            ret += [i]

    return ret

def ans(arr):

    old_arr = arr[:]

    assert(sum(arr) % 2 == 0)
    target = sum(arr) // 2

    arr = set(arr)
    mine = set()

    for i in range(0, 200):
        k = 2**i
        if k in arr:
            arr.remove(k)
            mine.add(k)

    arr = list(arr)
    arr = sorted(arr)

    chosen = []
    chosen_sum = 0

    while len(arr):
        if chosen_sum + arr[-1] <= target:
            chosen += [arr[-1]]
            chosen_sum += arr[-1]
            arr.pop()
        else:
            break

    gap = target - sum(chosen)

    mine = sorted(list(mine))

    while True:
        if len(mine) == 0: break
        if mine[-1] <= gap:
            gap -= mine[-1]
            chosen += [mine[-1]]
            mine.pop()
        else:
            arr += [mine[-1]]
            mine.pop()

    assert(set(old_arr) == set(chosen + arr))
    return chosen

T = read_int()
for _ in range(T):
    N = read_int()

    A = A_of(N)

    fprint(*A)

    B = read_int_list()

    fprint(*ans(A + B))