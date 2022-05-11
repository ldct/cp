#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def is_subsequence(needle, haystack):
    current_pos = 0
    for c in needle:
        current_pos = haystack.find(c, current_pos) + 1
        if current_pos == 0:
            return False
    return True

def ans(S1, S2):
    if is_subsequence(S1, S2):
        return len(S2) - len(S1)
    return "IMPOSSIBLE"

T = int(input())
for t in range(T):
    S1 = input()
    S2 = input()
    print("Case #" + str(t+1) + ": " + str(ans(S1, S2)))
