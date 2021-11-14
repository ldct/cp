#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def idx(c):
    return ord(c) - ord('a')

def cost1(a, b):
    a = idx(a)
    b = idx(b)
    diff = a - b
    diff %= 26
    diff += 26
    diff %= 26
    return min(diff, 26-diff)

def cost(a, F):
    ret = 27
    for b in F:
        ret = min(ret, cost1(a, b))
    return ret

def ans(S, F):
    F = set(F)
    return sum(cost(s, F) for s in S)

T = int(input())
for t in range(T):
    print("Case #" + str(t+1) + ": " + str(ans(input(), input())))
