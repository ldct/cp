#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def ans(S):
    for i in range(len(S)):
        if S[i] == '1':
            if i % 2 == 0:
                return "Takahashi"
            else:
                return "Aoki"
### CODE HERE

input()
print(ans(input()))