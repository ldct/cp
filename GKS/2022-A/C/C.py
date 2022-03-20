#!/usr/bin/env pypy3

from sys import stdin, stdout
from itertools import product

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def join(S, choice):
    arr = list(S)
    k = 0
    for i in range(len(S)):
        if arr[i] == '?':
            arr[i] = choice[k]
            k += 1
    return arr

def ok_slow(arr):
    for i in range(len(arr)+1):
        for j in range(i+1, len(arr)+1):
            ss = arr[i:j]
            if len(ss) >= 5 and (ss == ss[::-1]): return False
    return True

def ans(S):
    choices = S.count('?')
    for choice in product('01', repeat=choices):
        if ok_slow(join(S, choice)):
            return "POSSIBLE"
    return "IMPOSSIBLE"

T = int(input())
for t in range(T):
    input()
    S = input()
    print("Case #" + str(t+1) + ": " + str(ans(S)))
