#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

S = "989"

def ans(N):
    ret = list(S[0:N])
    d = 0
    while len(ret) < N:
        ret += [str(d)]
        d += 1
        d %= 10

    return ''.join(ret)

for _ in range(read_int()):
    N = read_int()
    print(ans(N))