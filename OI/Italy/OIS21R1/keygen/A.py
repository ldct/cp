#!/usr/bin/env python3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import product

### CODE HERE

def ok(assignment, S):
    S = S.replace('!', '_')
    env = dict()
    for i, v in enumerate(assignment):
        env[chr(ord('a') + i)] = v
        env['_' + chr(ord('a') + i)] = 1-v

    return 1 == (eval(S, env))

def ans(K, S):
    ret = 0
    for assignment in product([0,1], repeat=K):
        if ok(assignment, S):
            ret += 1
    return ret

for _ in range(read_int()):
    args = read_int(), input()
    print(ans(*args))
