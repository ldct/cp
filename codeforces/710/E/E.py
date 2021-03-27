#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(Q):
    ret = []
    last = -1
    for q in Q:
        if q > last:
            ret += [q]
            last = q
        else:
            ret += [0]

    unused = set(range(1, len(Q)+1))
    for r in ret:
        if r > 0:
            unused.remove(r)
    unused = sorted(list(unused))

    ret1 = ret[::]
    i = 0
    for j in range(len(ret1)):
        if ret1[j] == 0:
            ret1[j] = unused[i]
            i += 1


    return ret, ret1, ret2

for _ in range(read_int()):
    input()
    Q = read_int_list()
    print(ans(Q))