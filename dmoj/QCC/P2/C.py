#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

input()
X = read_int_list()
Y = read_int_list()

max_X = max(X)
max_Y = max(Y)
min_Y = min(Y)
min_X = min(X)

def ans_query(t, w):
    w -= 1
    if t == 1: return max(X[w], max_Y)
    if t == 2: return max(X[w], min_Y)
    if t == 3: return max(Y[w], max_X)
    if t == 4: return max(Y[w], min_X)

    return '?'

for _ in range(read_int()):
    query = read_int_tuple()
    print(ans_query(*query))