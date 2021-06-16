#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(N, M):
    if M == 1:
        if 0 <= N < 10:
            return N
    if N == 0:
        return -1
    ret = [1] + [0]*(M-1)
    N -= 1
    i = 1
    while N > 0 and i < M:
        ret[i] += min(9, N)
        N -= ret[i]
        i += 1
    if N > 0: return -1
    return ''.join(map(str, ret))
N, M = read_int_tuple()
print(ans(N, M))