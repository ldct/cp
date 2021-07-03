#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ends_in_1(N):
    if N == 11: return False
    return str(N)[-1] == "1"

def ends_in_234(N):
    if N in [12,13,14]: return False
    return str(N)[-1] in "234"

def ans(N):
    if N == 0:
        assert(False)
    elif ends_in_1(N):
        return f"{N} кочерга"
    elif ends_in_234(N):
        return f"{N} кочерги"
    else:
        return f"{N} кочерёг"

for N in 112,113,334:
    assert(ans(N) == f"{N} кочерги")
# N = read_int()
