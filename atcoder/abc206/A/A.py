#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

import math

p = math.floor(1.08 * read_int())
if p < 206:
    print("Yay!")
if p == 206:
    print("so-so")
if p > 206:
    print(":(")