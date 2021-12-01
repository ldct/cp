#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(S):
    possibles = set()
    for a in range(1, 1009):
        for b in range(1, 1009):
            possibles.add(4*a*b + 3*a + 3*b)
    return len([s for s in S if s not in possibles])


input()
print(ans(read_int_list()))