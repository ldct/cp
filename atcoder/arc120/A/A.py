#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

input()
A = read_int_list()

desc = A[0]
ones = A[0]
biggest = A[0]

print(desc+biggest)

i = 1
for a in A[1:]:
    i += 1
    ones += a
    desc += ones
    biggest = max(biggest, a)

    print(desc + (biggest*i))
