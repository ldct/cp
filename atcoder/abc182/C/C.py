#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans_weak(arr):
    if sum(arr) % 3 == 0: return 0
    if sum(arr) % 3 == 1:
        if arr.count(1) > 0: return 1
        if arr.count(2) > 0: return 2
        return -1
    if sum(arr) % 3 == 2:
        if arr.count(2) > 0: return 1
        if arr.count(1) > 0: return 2
        return -1

def ans(N):
    arr = list(map(int, N))
    N = len(arr)
    arr = [a%3 for a in arr if a % 3 != 0]
    ret = ans_weak(arr)
    if ret == N: return -1
    return ret

print(ans(input()))