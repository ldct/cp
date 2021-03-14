#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

N = read_int()

ret = 0

for i in range(0, 10):
    low = 10**(3*i)
    high = 10**(3*i+3)-1

    low = max(low, 1)
    high = min(high, N)

    if low > high: continue

    # print(low, high, i)

    ret += (high - low + 1)*i

print(ret)
