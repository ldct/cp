#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(budget, A):
    A.sort()
    ret = 0
    for a in A:
        # print(a, budget)
        if budget >= a:
            budget -= a
            ret += 1
    return ret

for _ in range(read_int()):
    N, L, R, K = read_int_tuple()
    A = read_int_list()
    A = [a for a in A if L <= a <= R]
    print(ans(K, A))