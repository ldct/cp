#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(S):
    num_O = 0
    num_X = 0
    num_inversions = 0
    ret = 0
    last = None
    for c in S:
        if c == 'F':
            ret += num_inversions
        if c == 'O':
            if last == 'X':
                num_inversions += 1
            num_O += 1
            last = 'O'

for t in range(read_int()):
    input()
    S = input()
    print(f"Case #{t+1}: {ans(S)}")