#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def fprint(*args):
	print(*args, flush=True)

def query(i, j):
    fprint("?", i+1, j+1)
    return read_int()

def query2(i, j):
    diff = query(i, j)
    y2 = query(i, j)
    assert (y2 % 2 == 0)
    y = y2 // 2
    return diff + y, y

### CODE HERE

N = read_int()

B = N // 2 if N % 2 == 0 else (N-1) // 2

ans = [-1] * N

for b in range(B):
    i = 2*b
    j = 2*b + 1
    x, y = query2(i, j)
    ans[i] = x
    ans[j] = y

if N % 2 == 1:
    i = N-2
    j = N-1
    diff = query(i, j)
    ans[j] = 2*ans[i] - diff

ans = ["!"] + ans
print(*ans)
