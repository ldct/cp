#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from itertools import chain, combinations
def subsets(iterable, low=0, high=None):
    "subsets([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    if high is None:
        high = len(s)
    return chain.from_iterable(combinations(s, r) for r in range(low, high+1))


N, M = read_int_tuple()
conditions = []
for _ in range(M):
    conditions += [read_int_tuple()]
K = read_int()
people = []
for _ in range(K):
    people += [read_int_tuple()]

def ans(a, b, people, conditions):
    dwb = set()
    for i in a:
        dwb.add(people[i][0])
    for i in b:
        dwb.add(people[i][1])

    ret = 0
    for x, y in conditions:
        if x in dwb and y in dwb:
            ret += 1
    return ret

ret = -1
S = set(range(len(people)))
for s in subsets(S):
    ret = max(ret, ans(s, S - set(s), people, conditions))

print(ret)
# print(people)