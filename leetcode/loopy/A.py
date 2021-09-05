#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from collections import defaultdict

def sim(N):
    num_visits = defaultdict(int)
    ret = []
    i = 0
    for _ in range(N):
        ret += [i]
        num_visits[i] += 1
        num_visits[i] %= 2
        if num_visits[i] == 1:
            i = 0
        else:
            i = i+1
    return ret

for k in range(5, 200):
    print(k, max(sim(k)))

print(max(sim(10**6)))