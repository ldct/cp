#!/usr/bin/env pypy3

input()

A = input().split()
A = list(map(int, A))

A = sorted(A)

tails = []

for a in A:
    set = False
    for i in range(len(tails)):
        if a > tails[i]:
            tails[i] = a
            set = True
            break
    if not set:
        tails += [a]

print(sum(tails))