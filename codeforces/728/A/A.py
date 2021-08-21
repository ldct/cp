#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(x):
    ret = list(range(1, x+1))
    if len(ret) % 2 == 0:
        for i in range(len(ret)):
            if i % 2 == 0:
                ret[i], ret[i+1] = ret[i+1], ret[i]
    else:
        for i in range(3, len(ret)):
            if i % 2 == 1:
                ret[i], ret[i+1] = ret[i+1], ret[i]
        ret[0] = 3
        ret[1] = 1
        ret[2] = 2

    return " ".join(map(str, ret))

for _ in range(read_int()):
    print(ans(read_int()))