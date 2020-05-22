#!/usr/bin/env python3

T = int(input())

def ans():
    n, k = input().split(' ')
    k = int(k)
    s = input()

    s = sorted(s)

    ret = []
    for i in range(k):
        ret += [[]]

    for i in range(k):
        ret[i] += [s[i]]

    if ret[0][0] != ret[-1][0]:
        return ret[-1][0]

    s = s[k:]
    if len(set(s)) > 1:
        return ret[0][0] + ''.join(s)

    for i in range(len(s)):
        ret[i % k] += [s[i]]

    return ''.join(ret[0])

    return '?'

for t in range(T):
    print(ans())