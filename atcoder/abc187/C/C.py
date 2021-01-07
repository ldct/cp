#!/usr/bin/env pypy3

from sys import stdin, stdout

def input():
    return stdin.readline().strip()

def read_line():
	return list(map(int, input().split()))

def read_int():
	return int(input())

### CODE HERE

strings = []
for _ in range(read_int()):
    strings += [input()]

A = set()
B = set()

for s in strings:
    if s[0] == '!':
        B.add(s[1:])
    else:
        A.add(s)

I = A & B

if len(I) == 0:
    print("satisfiable")
else:
    for i in I:
        print(i)
        break
