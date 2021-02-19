#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())
def multiset_of_counter(c):
    ret = []
    for k in c:
        ret += [k] * c[k]
    return ret
### CODE HERE

from collections import Counter

N, K = read_int_tuple()
A = read_int_list()

A = sorted(A)
ret = Counter()

ret[0] = K

for a in A:
    if ret[a] > 0:
        ret[a] -= 1
        ret[a+1] += 1
    # print(multiset_of_counter(ret))

ans = 0
for k in ret:
    ans += k*ret[k]

print(ans)