#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def ans(arr):
    arr.sort()
    need = 1
    for i, d in enumerate(arr):
        if need <= d:
            need += 1
    return need-1

T = int(input())
for t in range(T):
    input()
    print("Case #" + str(t+1) + ": " + str(ans(read_int_list())))
