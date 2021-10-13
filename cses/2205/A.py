#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(N):
    if N == 0: return [""]
    head = ans(N-1)
    tail = head[:][::-1]
    head = ["0" + h for h in head]
    tail = ["1" + h for h in tail]

    return head + tail

for s in ans(read_int()):
    print(s)