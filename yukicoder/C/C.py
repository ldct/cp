#!/usr/bin/env python3

MAJOR = set([0, 2, 4, 5, 7, 9, 11])

def subset(A, B):
    for a in A:
        if a not in B: return False
    return True

def ok(T, i):
    T = [((t - i % 12) + 12) % 12 for t in T]

    if subset(T, MAJOR):
        return True
    return False

def ans(T):
    candidates = [i for i in range(12) if ok(T, i)]
    if len(candidates) != 1: return -1
    return candidates[0]

input()
T = input().split(' ')
T = list(map(int, T))

print(ans(T))