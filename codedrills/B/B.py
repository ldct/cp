#!/usr/bin/env pypy3

def findindex(A, W):
    arr = []
    for a, w in zip(A, W):
        arr += [a - w]
    prefixes = [0]
    for a in arr:
        prefixes += [prefixes[-1] + a]
    if min(prefixes) >= 0: return 1

    ret = prefixes.index(min(prefixes))

    count = 0
    for i in range(len(A)):
        count += arr[(i + ret) % len(A)]
        if count < 0: return -1

    return ret
