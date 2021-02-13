#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def num_k(N, k):
    ret = 0
    base = k
    while True:
        if base > N: return ret
        ret += (N // base)
        base *= k

def ans(N):
    return min(num_k(N, 2), num_k(N, 5))

p = []
for i in range(1, 100):
    p += [ans(i)]

print(','.join(map(str, p)))
# print(ans(read_int()))
