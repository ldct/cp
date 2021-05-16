#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

N, M = read_int_tuple()
costs = []
for _ in range(N):
    costs += [read_int_tuple()]
costs = sorted(costs)

spent = 0
i = 0

while M:
    each, upto = costs[i]
    buy = min(M, upto)
    # print("buying", buy)
    M -= buy
    spent += each*buy
    i += 1

print(spent)
