#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(A):
    if len(A) == 2:
        (_, i) = sorted(A)[0]
        return i

    nA = []
    for i in range(len(A) // 2):
        nA += [sorted(A[2*i:2*i+2])[1]]

    return ans(nA)

input()
A = read_int_list()
A = [(e,i+1) for (i,e) in enumerate(A)]
print(ans(A))