#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(K, arr):
    if K not in arr: return [0]
    i = arr.index(K)
    left, right = arr[0:i], arr[i:]
    right = right[1:]
    return (sum(left), sum(right))

for _ in range(read_int()):
    N, K = read_int_tuple()
    arr = read_int_list()
    print(*ans(K, arr))