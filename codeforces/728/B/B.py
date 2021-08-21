#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(lst):

    index = dict()
    for i in range(len(lst)):
        index[lst[i]] = i + 1

    sl = set(lst)

    target = 2*max(lst)
    ret = 0

    def ok(ai, aj):
        if not (ai in sl and aj in sl): return False
        i = index[ai]
        j = index[aj]
        return i < j and i + j == ai*aj

    for ai in range(1, target+10):
        for aj in range(ai+1, target+10):
            if ai*aj > target: break
            if ok(ai, aj): ret += 1
            if ok(aj, ai): ret += 1

    return ret

if True:
    for _ in range(read_int()):
        input()
        print(ans(read_int_list()))
else:
    N = 100000
    tc = list(range(1, N))
    print(ans(tc))