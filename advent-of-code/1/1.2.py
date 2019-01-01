#!/usr/bin/env python3

from collections import defaultdict

with open('./input.txt') as f:
    lines = list(int(line) for line in f.readlines())

def first_repeat(elems):
    freqs = defaultdict(int)

    freqs[0] = 1
    curr = 0

    while True:
        for delta in lines:
            curr += delta
            freqs[curr] += 1
            if freqs[curr] == 2:
                return(curr)

print(first_repeat(lines))