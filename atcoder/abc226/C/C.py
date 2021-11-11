#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

dependencies = []
times = []
N = read_int()
for _ in range(N):
    line = read_int_list()
    times += [line[0]]
    dependencies += [[i-1 for i in line[2:]]]

must_learn = [False]*N
must_learn[-1] = True
for i in range(len(must_learn)-1, -1, -1):
    if must_learn[i]:
        for d in dependencies[i]:
            must_learn[d] = True

print(sum(times[i] for i in range(N) if must_learn[i]))
