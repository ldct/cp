#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def find(arr, target, start):
    for i in range(start, len(arr)):
        if arr[i] == target: return i
    return None

def ans(A, B):
    ret = 0
    i = 0
    while i < len(A):
        if A[i] == B[i]:
            i += 1
            continue
        j = find(A, B[i], i)
        if j is None: return -1
        A[i], A[j] = A[j], A[i]
        ret += (j - i)
    return ret

def ans_str(S):
    S = [0 if s == "I" else 1 for s in S]
    target = [i % 2 for i in range(len(S))]
    return ans(S, target)

if True:
    input()
    S = input()
    print(ans_str(S))