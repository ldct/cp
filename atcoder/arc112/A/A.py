#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(L, R):
    last = R - 2*L + 1
    if last < 1: return 0
    return (1 + last)*(last) // 2
    # ret = 0
    # for i in range(2*L, R+1):
    #     ret += i - 2*L + 1
    # return ret

for _ in range(read_int()):
    L, R = read_int_tuple()
    print(ans(L, R))