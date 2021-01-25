#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

N, X = read_int_tuple()
X *= 100

bottles = []

for _ in range(N):
    V, P = read_int_tuple()
    bottles += [V*P]

ans = None
for i, e in enumerate(bottles):
    if e > X:
        ans = i+1
        break
    else:
        X -= e

if ans is not None:
    print(ans)
else:
    print(-1)