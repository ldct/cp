#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

N, Q = read_int_tuple()

A = read_int_list()

from collections import defaultdict

freq = defaultdict(int)

for a in A:
    freq[a] += 1

for _ in range(Q):
    t, p = read_int_tuple()
    if t == 1:
        n = freq[p]
        freq[p] = 0

        freq[p // 2] += n
        freq[(p+1) // 2] += n
    elif t == 2:
        print(freq[p])
    else:
        assert(False)