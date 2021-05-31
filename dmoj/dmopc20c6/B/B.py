#!/usr/bin/env pypy3

import sys
from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

input()
A = read_int_list()
B = read_int_list()

A_indices = []
B_indices = []

for i, a in enumerate(A):
    if a == 0: A_indices += [i]

for i, b in enumerate(B):
    if b == 0: B_indices += [i]

if len(A_indices) != len(B_indices):
    print(-1)
    sys.exit(0)

for i, j in zip(A_indices, B_indices):
    if i < j:
        print(-1)
        sys.exit(0)

# print(A_indices)
# print(B_indices)

ret = []

i = 0
while i < len(A_indices):
    if A_indices[i] == B_indices[i]:
        i += 1
        continue

    j = i
    while j+1 < len(B_indices) and B_indices[j+1] == B_indices[j] + 1:
        j += 1

    ret += [(B_indices[i]+1, A_indices[j]+1)]
    # print("move", B_indices[i]+1, A_indices[j]+1)

    i = j+1

print(len(ret))
for op in ret:
    print(*op)