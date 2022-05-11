#!/usr/bin/env pypy

from __future__ import division, print_function

import itertools
import sys

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

MODULUS = 10**9+7

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import product

def cdiv(x, y):
    return x // y if x % y == 0 else x // y + 1

def is_palindrome(s):
    return s == s[::-1]

def ans_slow(K, S):
    N = len(S)
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"[0:K]

    ret = 0
    for s in product(ALPHABET, repeat=N):
        ss = ''.join(s)
        if ss < S and is_palindrome(ss):
            # print(ss)
            ret += 1

    return ret

def flip_front(S):
    N = len(S)
    if N % 2 == 0:
        S = S[0:N//2]
        return S + S[::-1]
    S = S[0:N//2+1]
    return S + S[::-1][1:]

def ans(K, S):
    N = len(S)

    ret = 0
    for i in range(N):
        # print("i=", i)
        this_less = ord(S[i]) - ord('a')
        to_add = 0
        if i < N//2:
            free = N-2*(i+1)
            free = cdiv(free, 2)
            to_add = this_less * pow(K, free, MODULUS)
        elif N % 2 == 1 and i == N//2:
            to_add = this_less * 1
        ret += to_add
        ret %= MODULUS

        # print("i=", i, "adding", to_add)

    if flip_front(S) < S:
        # print("suplement")
        ret += 1
        ret %= MODULUS

    return ret

if False:
    K = 5
    S = "baed"
    print(ans_slow(K, S))
    print(ans(K, S))
elif False:
    import random
    for _ in range(100):
        K = 26
        S = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz"[:K]) for _ in range(10**5))
        print(ans(K, S))
else:
    T = int(input())
    for t in range(T):
        N, K = read_int_tuple()
        S = input()
        print("Case #" + str(t+1) + ": " + str(ans(K, S)))
