#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

N, W = read_int_tuple()
cheeses = [read_int_tuple() for _ in range(N)]
cheeses = sorted(cheeses)[::-1]

ret = 0
i = 0
while i < len(cheeses) and W > 0:
    use = min(cheeses[i][1], W)
    W -= use
    ret += use*cheeses[i][0]
    i += 1

print(ret)