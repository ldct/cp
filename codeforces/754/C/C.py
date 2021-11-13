#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from collections import Counter

def good(S, i, j):
    j = min(j, len(S))
    if j - i < 2: return False
    num_a = 0
    num_b = 0
    num_c = 0
    for k in range(i, j):
        if S[k] == 'a': num_a += 1
        if S[k] == 'b': num_b += 1
        if S[k] == 'c': num_c += 1
    return num_a > max(num_b, num_c)

def ans(S):
    for offset in [2,3,4,5,6,7]:
        for i in range(len(S)+1):
            if good(S, i, i+offset): return offset
    return -1

if False:
    import random
    for l in range(3, 20):
        print("l=", l)
        for _ in range(100000):
            tc = "".join(random.choice("abc") for _ in range(10))
            if not (ans(tc) == ans_slow(tc)):
                print(tc)
                break
elif True:
    tc = "abc"*(10**6)
    print(1)
    print(1)
    print(tc)
else:
    for _ in range(read_int()):
        input()
        print(ans(input()))