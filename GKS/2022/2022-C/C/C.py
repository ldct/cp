#!/usr/bin/env python3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import Counter, defaultdict, deque

for i in range(100000):
    import random
    tc = [(random.randint(1, 100), random.randint(0, 1)) for _ in range(100)]
    print(i)
    ans(tc)

T = int(input())
for t in range(T):
    N, L = read_int_tuple()
    ants = []
    for _ in range(N):
        ants += [read_int_tuple()]
    print("Case #" + str(t+1) + ": " + str(ans(L, ants)))
