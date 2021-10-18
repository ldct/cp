#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def shifts(s):
    ret = []
    for _ in range(len(s) + 4):
        s = s[1:] + s[0]
        ret += [s]
    return ret

S = input()
arr = shifts(S)
arr.sort()
print(arr[0])
print(arr[-1])