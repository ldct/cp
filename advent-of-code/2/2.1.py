#!/usr/bin/env python3

from collections import defaultdict

with open('./input.txt') as f:
    words = f.read().split('\n')[:-1]

def repeats(word, count):
    freqs = defaultdict(int)
    for c in word:
        freqs[c] += 1
    for c in freqs:
        if freqs[c] == count:
            return True
    return False

def checksum(words):
    num_2 = 0
    num_3 = 0
    for word in words:
        if repeats(word, 2): num_2 += 1
        if repeats(word, 3): num_3 += 1
    return num_2 * num_3

print(checksum(words))

