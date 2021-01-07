#!/usr/bin/env pypy3

from sys import stdin, stdout

def input():
    return stdin.readline().strip()

def read_line():
	return list(map(int, input().split()))

def read_int():
	return int(input())

### CODE HERE

def s(num):
    return sum(map(int, num))

[A, B] = input().split()
print(max(s(A), s(B)))