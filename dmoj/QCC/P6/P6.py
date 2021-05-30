#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

input()
arr = read_int_list()

right = [0]
for i in range(len(arr)-1):
    right += [right[-1] + (i+1)*abs(arr[i+1] - arr[i])]

left = [0]
arr = arr[::-1]
for i in range(len(arr)-1):
    left += [left[-1] + (i+1)*abs(arr[i+1] - arr[i])]
left = left[::-1]

for _ in range(read_int()):
    q = read_int()-1
    print(left[q] + right[q])
