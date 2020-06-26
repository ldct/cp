#!/usr/bin/env pypy3

import array

def ans(s):
    counts = []

    count = 0
    for i, c in enumerate(s):
        if c == '-':
            count -= 1
        elif c == '+':
            count += 1
        else:
            assert(False)
        counts += [(count, i+1)]

    counts += [(float("-inf"), len(s))]

    counts = sorted(counts) + [(0, 0)]

    prevCount = None

    ret = 0

    for count, l in counts:
        if count >= 0: break
        if count == prevCount: continue
        ret += l
        prevCount = count

    return ret

T = int(input())

for _ in range(T):
    s = input()
    print(ans(s))
