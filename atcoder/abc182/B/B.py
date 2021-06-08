#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def argmax_all(d):
    am = None
    for k in d:
        if am is None or d[k] > d[am]:  am = k
    ret = set()
    for k in d:
        if d[k] == d[am]: ret.add(k)
    return ret

input()
A = read_int_list()
def gcdness(k):
    return len([a for a in A if a % k == 0])

print(max(argmax_all({k : gcdness(k) for k in range(2, 1009)})))
