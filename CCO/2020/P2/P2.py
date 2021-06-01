#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def rightmost(A, B):
    for j in range(len(A)-1, -1, -1):
        if B[j] < A[j]: return j

def leftmost(A, i, cap):
    for k in range(i, -1, -1):
        if A[k] <= cap:
            return k

def ans(B):
    A = list(range(1, len(B) + 1))

    ret = 0

    while True:
        # print(B)
        # print(A)

        j = rightmost(A, B)
        if j is None: return ret

        i = leftmost(A, j, B[j])
        if i is None: return -1

        for t in range(i, j):
            ret += 1
            A[t], A[t+1] = A[t+1], A[t]

    return ret

input()
B = read_int_list()
print(ans(B))
