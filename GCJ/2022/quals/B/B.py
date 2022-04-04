#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def ans(arr):
    bounds = [10**6]*4
    for row in arr:
        for i in range(len(row)):
            bounds[i] = min(bounds[i], row[i])
    if sum(bounds) < 10**6: return "IMPOSSIBLE"

    ret = []

    for s in bounds:
        ret += [
            min(s, 10**6 - sum(ret))
        ]

    return " ".join(map(str, ret))

T = int(input())
for t in range(T):
    arr = [read_int_tuple(), read_int_tuple(), read_int_tuple()]
    print("Case #" + str(t+1) + ": " + str(ans(arr)))
