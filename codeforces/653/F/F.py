#!/usr/bin/env pypy3

def ans(A):
    if len(A) != len(set(A)): return ['?', '?']

    pos_of = dict()

    for i, e in enumerate(sorted(A)):
        pos_of[e] = i+1

    A = [pos_of[a] for a in A]

    return [A]


T = int(input())

for _ in range(T):
    input()
    A = input().split(' ')
    A = list(map(int, A))
    print(*ans(A))