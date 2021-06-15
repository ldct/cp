#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

input()
A = read_int_list()

def score(x):
    return sum(x + a - min(a, 2*x) for a in A)

low = 0
high = 2*max(A)

for _ in range(40):
    d = (high - low) / 3

    m1 = low + d
    m2 = low + 2*d

    if score(m1) > score(m2):
        low = m1
    else:
        high = m2

print(score(low) / len(A))