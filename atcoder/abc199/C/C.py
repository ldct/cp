#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

N = read_int()
S = input()

S = list(S)
flipped = False

def flip(x):
    if x < N: return N + x
    return x - N

def swap(A, B):
    if flipped:
        A = flip(A)
        B = flip(B)

    S[A], S[B] = S[B], S[A]



for _ in range(read_int()):
    T, A, B = read_int_tuple()
    if T == 2:
        flipped = not flipped
    elif T == 1:
        A -= 1
        B -= 1
        swap(A, B)

if flipped:
    S = S[N:] + S[0:N]

print(''.join(S))