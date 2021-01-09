#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from itertools import permutations

def summary(arr):
    arr = sorted(arr)
    s = sum(arr)
    return (s, -s, s - 2*arr[0], len(arr))

input()
s1 = summary(read_int_list())
s2 = summary(read_int_list())
s3 = summary(read_int_list())

def ok1(s, t):
    if t == "+-": return s[-1] > 1
    return True

def ok2(t1, t2):
    if t1 == "+": return t2 == "-"
    if t1 == "-": return t2 == "+"
    return True

def score_permutation(s1, s2, s3):
    ret = -1
    for t1 in ["+", "-", "+-"]:
        for t2 in ["+", "-", "+-"]:
            for t3 in ["+", "-", "+-"]:
                if not(ok1(s1, t1)): continue
                if not(ok1(s2, t2)): continue
                if not(ok1(s3, t3)): continue
                if not (ok2(t1, t2)): continue
                if not (ok2(t2, t3)): continue

                candidate = max(ret,
                    s1[["+", "-", "+-"].index(t1)] +
                    s2[["+", "-", "+-"].index(t2)] +
                    s3[["+", "-", "+-"].index(t3)]
                )
                # print(candidate, t1, t2, t3)
                ret = max(ret, candidate)
    return ret

ret = -1
for p in permutations([s1, s2, s3]):
    ret = max(ret, score_permutation(*p))

print(ret)