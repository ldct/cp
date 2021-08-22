#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def maxMatrixSum(matrix):
    arr = []
    for row in matrix:
        arr += row

    if 0 in arr:
        return sum([abs(r) for r in arr])

    num_neg = 0
    for x in arr:
        if x < 0: num_neg += 1

    if num_neg % 2 == 0:
        return sum([abs(r) for r in arr])

    arr = sorted(list(abs(r) for r in arr))
    arr[0] *= -1
    return sum(arr)

m = [[10,-6,-6,-8],[-3,-7,-8,-9],[-4,-8,-5,-8],[-9,-9,-6,-8]]
print(maxMatrixSum(m))