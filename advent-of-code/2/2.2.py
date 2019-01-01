#!/usr/bin/env python3

from collections import defaultdict

with open('./input.txt') as f:
    words = f.read().split('\n')[:-1]

def num_diffs(w1, w2):
    assert(len(w1) == len(w2))
    ret = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]: ret += 1
    return ret

def differs_in_two(words):
    for w1 in words:
        for w2 in words:
            if num_diffs(w1, w2) == 1:
                return w1, w2

def sub_common(w1, w2):
    assert(len(w1) == len(w2))
    ret = []
    for i in range(len(w1)):
        if w1[i] == w2[i]: ret += w1[i]
    return ''.join(ret)

print(sub_common(*differs_in_two(words)))
