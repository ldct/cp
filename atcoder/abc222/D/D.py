#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

MODULUS = 998244353

N = read_int()
A = read_int_list()
B = read_int_list()

def prefix(arr):
    ret = [0]
    for a in arr:
        ret += [ret[-1] + a]
    return ret

def psum(p, t, a, b):
    if not (a <= b): return 0
    return p[b] - p[a]

table = [1]*3009
for i in range(N-1, -1, -1):
    # print(table)
    new_table = []
    p = prefix(table)

    for lb in range(len(table)):
        new_table += [psum(
            p, table, max(lb, A[i]), B[i]+1
        ) % MODULUS]
    table = new_table

print(table[0])