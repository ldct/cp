#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

# TODO: use class

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def ans_slow(s, T):
    ss = set(s)
    for t in T:
        if t not in ss: return -1

    i = 0
    for t in T:
        while s[i % len(s)] != t: i+= 1
        i += 1

    return i

def ans(s, T):
    ss = set(s)
    for t in T:
        if t not in ss: return -1

    right = []

    s2 = s + s

    for c in s2:
        right += [None]

    last = [float("inf")]*26

    for i in range(len(s2)-1, -1, -1):
        right[i] = last.copy()
        last[ord(s2[i]) - ord('a')] = i

    for i, d in enumerate(right):
        for a in range(len(d)):
            d[a] -= i

    right2 = []
    for i in range(len(s)):
        m = [float("inf")]*26
        for a in ALPHABET:
            g = right[i][ord(a) - ord('a')]
            if g != None:
                m[ord(a) - ord('a')] = min(m[ord(a) - ord('a')], g)
            g = right[i + len(s)][ord(a) - ord('a')]
            if g != None:
                m[ord(a) - ord('a')] = min(m[ord(a) - ord('a')], g)

        right2 += [m]

    right = right2

    i = 0
    for t in T:
        if s[i % len(s)] == t:
            i += 1
        else:
            i += right[i % len(s)][ord(t) - ord('a')]
            i += 1

    return i

if False:
    import random
    s = ''.join(random.choice(ALPHABET) for _ in range(5*10**5))
    T = ''.join(random.choice(ALPHABET) for _ in range(5*10**5))
    print(ans(s, T))
else:
    input()

    s = input()
    T = input()

    print(ans(s, T))