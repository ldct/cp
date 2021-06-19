#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from functools import lru_cache

@lru_cache(None)
def p1_wins(N):
    for i in range(2, N):
        if N % i == 0 and not p1_wins(N - i): return True
    return False

def p1_wins_fast(N):
    e = len("{0:b}".format(N)) - 1
    if N == 2**e and e % 2 == 1: return False
    return N % 2 == 0 and N >= 4

if True:
    N = 10000
    for i in range(1, N):
        if i % 100 == 0: print(i / N)
        if p1_wins(i) != p1_wins_fast(i):
            print(i)
else:
    for _ in range(read_int()):
        print("Alice" if p1_wins_fast(read_int()) else "Bob")