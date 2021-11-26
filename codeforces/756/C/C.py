#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import deque

### CODE HERE

def ans(arr):
    M = max(arr)
    if M not in [arr[0], arr[-1]]: return [-1]
    arr = deque(arr)
    ret = deque([])

    if arr[0] == M:
        ret.append(arr.popleft())
    elif arr[-1] == M:
        ret.append(arr.pop())

    while len(arr):
        if len(arr) == 1:
            ret.append(arr.popleft())
        else:
            a = arr.popleft()
            b = arr.pop()
            ret.appendleft(a)
            ret.append(b)

    return ret

for _ in range(read_int()):
    input()
    print(*ans(read_int_list()))