#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(M, pairs):

    singles = []
    doubles = []
    for (a, b) in pairs:
        if b == 1:
            singles += [a]
        else:
            doubles += [a]

    singles = sorted(singles)[::-1]
    doubles = sorted(doubles)[::-1]

    i = 0
    j = 0

    s = 0
    while j < len(doubles) and s < M:
        s += doubles[j]
        j += 1

    j -= 1

    ret = float("inf")

    while i <= len(singles):
        while j != -1 and s - doubles[j] >= M:
            s -= doubles[j]
            j -= 1
        if s >= M:
            ret = min(ret, i + 2*(j+1))
        else:
            pass
            # print(i, j, s, "nope")

        if i < len(singles):
            s += singles[i]

        i += 1

    if ret == float("inf"): return -1
    return ret

for _ in range(read_int()):
    n, m = read_int_tuple()
    A = read_int_list()
    B = read_int_list()
    print(ans(m, list(zip(A, B))))