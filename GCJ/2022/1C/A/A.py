#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def left_interior(s):
    i = 0
    while i != len(s) and s[i] == s[0]:
        i += 1
    return s[i:]

def interior(s):
    return left_interior(left_interior(s)[::-1])

def middles(S, c):
    ret = []
    for i, s in enumerate(S):
        if c in interior(s):
            ret += [i]
    return ret

def merge_long(S):
    for i in range(len(S)):
        for j in range(len(S)):
            if i == j: continue
            if S[i][-1] == S[j][0] and 1 == len(set(S[j])):
                S[i] += S[j]
                del S[j]
                return merge_long(S)
    return S

def merge(S):
    S = merge_long(S)
    for i in range(len(S)):
        for j in range(len(S)):
            if i == j: continue
            if S[i][-1] == S[j][0]:
                S[i] += S[j]
                del S[j]
                return S
    return None


def contains(S, c):
    return [i for (i, s) in enumerate(S) if c in s]

def is_impossible(S):
    for c in ALPHABET:
        r = contains(S, c)
        if len(set(r)) > 1:
            return True
    return False

def string_is_impossible_c(S, c):
    indexes = [i for (i, s) in enumerate(S) if s == c]
    if len(indexes) == 0: return False
    return indexes != list(range(min(indexes), max(indexes)+1))

def string_is_impossible(S):
    for c in ALPHABET:
        if string_is_impossible_c(S, c):
            return True
    return False

def ans(S):
    S = S[:]
    S = _ans(S)
    if S == False: return False
    if string_is_impossible(S):
        return False
    return S

def _ans(S):
    while len(S) > 1:
        r = merge(S)
        if r is not None:
            S = r
            continue

        if is_impossible(S):
            return False
        else:
            S = ''.join(S)
            return S

    return S[0]

def ans_slow(S):
    for ss in permutations(S):
        if not string_is_impossible(''.join(ss)):
            return ''.join(ss)
    return False

def eq(a, b):
    if a == False: return b == False
    if b == False: return a == False
    return True

if False:
    tc = ["AE", "EF", "EE"]
    for p in permutations(tc):
        print(ans(list(p)))
elif True:
    import random
    for _ in range(100000):
        tc = [''.join(random.choice('ABCDEFGHIJK') for _ in range(3)) for _ in range(5)]
        if not eq(ans(tc), ans_slow(tc)):
            assert(False)
            break
else:
    T = int(input())
    for t in range(T):
        N = read_int()
        S = input().split()

        r = ans(S)
        if r == False: r = "IMPOSSIBLE"
        print("Case #" + str(t+1) + ": " + str(r))
