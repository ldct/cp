#!/usr/bin/env python3

T = int(input())

def ans(A):

    A = A + "0"

    blocks = []

    last = 0

    for c in A:
        if c == '0':
            if last > 0:
                blocks += [last]
            last = 0
        else:
            last += 1

    blocks = sorted(blocks)[::-1]

    return sum(blocks[::2])


for t in range(T):
    print(ans(input()))
