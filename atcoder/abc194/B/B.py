#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

times = [read_int_tuple() for _ in range(read_int())]
# print(times)

ret = min(map(sum, times))

for i in range(len(times)):
    for j in range(i+1, len(times)):
        ret = min(ret,
            max(times[i][0], times[j][1]),
            max(times[i][1], times[j][0])
        )

print(ret)