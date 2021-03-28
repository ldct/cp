#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def f(arr):
    n = len(arr)
    ret = []
    for i in range(len(arr)):
        if i % 2 == 0:
            ret += [arr[i // 2]]
        else:
            ret += [arr[n // 2 + (i-1) // 2]]
    return ret

def ans(n):
    arr = list(range(0, n))
    # print(arr)
    arr = f(arr)
    # print(arr)
    ret = 1
    while arr[1] != 1:
        ret += 1
        arr = f(arr)
        # print(arr)
    return ret

for n in range(998, 1000, 2):
    print(n, ans(n))
