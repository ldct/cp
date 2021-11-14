#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def f(S):
    for i in range(10):
        j = (i+1)%10
        k = (i+2)%10
        S = S.replace(f"{i}{j}", f"{k}")
    return S

def f_pipe(S):
    for i in range(9):
        j = (i+1)%10
        k = (i+2)%10
        S = S.replace(f"{i}{j}", f"{k}")
    return S

def next_to(a, b):
    return (a+1)%10 == b

def f_fast(S):
    ret = []
    curr = S[0]
    i = 1
    while i < len(S):
        if next_to(curr, S[i]):
            curr = (curr+2) % 10
            i += 1
        else:
            ret += [curr]
            curr = S[i]
            i += 1
    ret += [curr]
    return ret

def ans(S):
    S = list(map(int, S))
    while True:
        next_S = f_fast(S)
        if next_S == S: return ''.join(map(str, S))
        S = next_S

def ans_slow(S):
    while True:
        next_S = f(S)
        if next_S == S: return S
        S = next_S

if True:
    print(ans("6568"), ans_slow("6568"))
elif True:
    import random
    for _ in range(1000):
        tc = [random.randint(0, 9) for _ in range(4)]
        tc = ''.join(map(str, tc))
        if tc == "901": continue
        if not (ans(tc) == ans_slow(tc)):
            print(tc)
            break

else:
    T = int(input())
    for t in range(T):
        input()
        S = input()
        print("Case #" + str(t+1) + ": " + str(ans(S)))
