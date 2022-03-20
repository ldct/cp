#!/usr/bin/env pypy3

from sys import stdin, stdout
from itertools import product

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def join(S, choice):
    arr = list(S)
    k = 0
    for i in range(len(S)):
        if arr[i] == '?':
            arr[i] = choice[k]
            k += 1
    return ''.join(arr)

forbidden = []

for ss in product('01', repeat=5):
    if ss == ss[::-1]:
        forbidden += [ss + ('0',)]
        forbidden += [ss + ('1',)]
        forbidden += [('0',) + ss]
        forbidden += [('1',) + ss]

for ss in product('01', repeat=6):
    if ss == ss[::-1]:
        forbidden += [ss]

forbidden = [''.join(s) for s in forbidden]
forbidden = set(forbidden)

def is_ok(s):
    for f in forbidden:
        if f in s: return False
    return True

def ans_fast(S):
    head = S[0:12]

    ok = set()

    choices = head.count('?')
    for choice in product('01', repeat=choices):
        ok.add(join(head, choice))

    ok = set(s for s in ok if is_ok(s))

    if len(ok) == 0: return "IMPOSSIBLE"

    for c in S[12:]:
        next = [c]
        if c == '?':
            next = ['0', '1']

        next_ok = set()
        for s in ok:
            for n in next:
                next_ok.add(s[1:] + n)

        ok = next_ok
        ok = set(s for s in ok if is_ok(s))

        if len(ok) == 0: return "IMPOSSIBLE"

    return "POSSIBLE"

def ok_slow(arr):
    for i in range(len(arr)+1):
        for j in range(i+1, len(arr)+1):
            ss = arr[i:j]
            if len(ss) >= 5 and (ss == ss[::-1]): return False
    return True

def ans(S):
    choices = S.count('?')
    for choice in product('01', repeat=choices):
        if ok_slow(join(S, choice)):
            return "POSSIBLE"
    return "IMPOSSIBLE"

import random
for _ in range(100):
    tc =
# T = int(input())
# for t in range(T):
#     input()
#     S = input()
#     print("Case #" + str(t+1) + ": " + str(ans_fast(S)))
