#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(have, boosts):
    boosts = sorted(boosts)
    last = 0
    for at, boost in boosts:
        if at - last > have:
            return last+have
        have -= (at - last)
        last = at
        have += boost
    return last+have

N, K = read_int_tuple()
boosts = []
for _ in range(N):
    boosts += [read_int_tuple()]
print(ans(K, boosts))
