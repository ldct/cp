#!/usr/bin/env python3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

n, a_num, b_num = read_int_tuple()
A = read_int_list()
B = read_int_list()

start = sum(A)

switches = [b - a for a, b in zip(A, B)]
switches = sorted(switches)[::-1]

print(start + sum(switches[0:b_num]))