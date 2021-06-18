#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

x = read_int()
ans = 0
ans += 2*(x // 11)
x %= 11
if x > 6:
    x -= 6
    ans += 1
if x > 0:
    ans += 1
print(ans)