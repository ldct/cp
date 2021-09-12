#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

P = read_int_list()
print(''.join(ALPHABET[i-1] for i in P))