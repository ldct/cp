#!/usr/bin/env python3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

low = "abcdefghijklmnopqrstuvwxyz"
high = low.upper()

def miss(S, alphabet):
    for c in alphabet:
        if c in S: return False
    return True

def ans(S):
    if miss(S, low):
        S += 'a'
    if miss(S, high):
        S += 'A'
    if miss(S, '0123456789'):
        S += '0'
    if miss(S, '#@*&'):
        S += '#'
    while len(S) < 7:
        S += 'x'
    return S

T = int(input())
for t in range(T):
    N = input()
    S = input()
    print("Case #" + str(t+1) + ": " + str(ans(S)))
