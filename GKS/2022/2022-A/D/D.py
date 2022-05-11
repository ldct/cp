#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def interesting(N):
    S = str(N)
    A = 1
    for c in S:
        A *= int(c)
    return (A % sum(map(int, S))) == 0

ret = [0]
MAX = 10**5+9
for i in range(1, MAX):
    if interesting(i):
        ret += [1 + ret[-1]]
    else:
        ret += [ret[-1]]

def ans(a, b):
    return ret[b] - ret[a-1]

T = int(input())
for t in range(T):
    a, b = read_int_tuple()
    print("Case #" + str(t+1) + ": " + str(ans(a, b)))
