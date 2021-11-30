#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans_j(arr, j):
    for i in range(len(arr)):
        if i == j: continue
        while arr[i] % 2 == 0:
            arr[i] = arr[i] // 2
            arr[j] *= 2
    return sum(arr)

def ans(arr):
    return max(ans_j(arr, j) for j in range(len(arr)))

for _ in range(read_int()):
    input()
    print(ans(read_int_list()))