#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import defaultdict

### CODE HERE

def cdiv(x, y):
    return x // y if x % y == 0 else x // y + 1

S = input()

mismatches = defaultdict(int)
total_mismatches = 0
ret = 0

for b, c in zip(S, sorted(S)):
    if b == c: continue
    mismatches[b + c] += 1
    total_mismatches += 1

while total_mismatches:
    swapped = False
    for a in 'LMS':
        for b in 'LMS':
            if a == b: continue
            if mismatches[a+b] > 0 and mismatches [b+a] > 0:
                mismatches[a+b] -= 1
                mismatches[b+a] -= 1
                total_mismatches -= 2
                ret += 1
                swapped = True
                break
    if swapped: continue

    for a, b, c in ["LMS", "LSM", "MLS", "MSL", "SML", "SLM"]:
        if mismatches[a+b] > 0 and mismatches[c+a] > 0:
            mismatches[a+b] -= 1
            mismatches[c+a] -= 1
            mismatches[c+b] += 1
            ret += 1
            total_mismatches -= 1
            break

print(ret)