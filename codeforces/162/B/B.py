#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

arr = [read_int() for _ in range(read_int())]

y = 0
ret = 0

for i,a in enumerate(arr):
    if y > a:
        # print(f"move to jump height in {a-y} moves")
        ret += y - a
        y = a
    else:
        pass
        # print("move to jump height in 0 moves")

    if i > 0:
        # print("jump")
        ret += 1

    # print(f"move to top in {a-y} moves")
    ret += a-y
    y = a

    # print(f"eat in 1 moves")
    ret += 1

print(ret)