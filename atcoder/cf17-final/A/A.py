#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

import re

S = input()
regex = "^A?KIHA?BA?RA?$"
if re.match(regex, S) is not None:
    print("YES")
else:
    print("NO")
