#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(N):
    def moves(a, b, c, X):
        if X == 1:
            return [(a, b)]
        return moves(a, c, b, X-1) + [(a, b)] + moves(c, b, a, X-1)
    return moves(1, 3, 2, N)

N = read_int()
r = ans(N)
print(len(r))
for p in r:
    print(*p)
