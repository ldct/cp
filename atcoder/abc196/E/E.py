#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

N = read_int()

offset = 0
b = float("-inf")
c = float("inf")

for _ in range(N):
    a, t = read_int_tuple()
    if t == 1:
        offset += a
        b += a
        c += a
    elif t == 2:
        if b == c:
            b = max(b, a)
            c = b
        else:
            if a < c:
                b = max(a,b)
            else:
                b = max(a,b)
                c = b
    elif t == 3:
        if b == c:
            b = min(b,a)
            c = b
        else:
            c = min(c,a)

# print(offset, b, c)

Q = read_int()
X = read_int_list()
for x in X:
    x += offset
    x = max(x, b)
    x = min(x, c)
    print(x)