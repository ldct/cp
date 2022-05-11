#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def add(arr, to_add):
    candidates = []
    for i in range(len(arr)+1):
        a2 = arr[:]
        a2.insert(i, to_add)
        candidates += [a2]
    return min(candidates)

def add_fast(arr, to_add):
    S1 = arr[:]
    i = 0
    while i < len(S1) and S1[i] <= to_add:
        i += 1
    S1.insert(i, to_add)
    return S1

def ans(S1):
    S1 = list(map(int, S1))
    to_add = (9 - (sum(S1) % 9)) % 9
    if to_add == 0:
        S1.insert(1, to_add)
    else:
        S1 = add_fast(S1, to_add)
    return ''.join(map(str, S1))

T = int(input())
for t in range(T):
    S1 = input()
    print("Case #" + str(t+1) + ": " + str(ans(S1)))
