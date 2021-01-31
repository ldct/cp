#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

N, S, D = read_int_tuple()
spells = 0
for _ in range(N):
    x, y = read_int_tuple()
    if x >= S: continue
    if y <= D: continue
    spells += 1

if spells > 0:
    print("Yes")
else:
    print("No")
