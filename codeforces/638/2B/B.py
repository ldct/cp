#!/usr/bin/env python3

T = int(input())

def uniqs(l):
    seen = set()
    ret = []
    for e in l:
        if e not in seen:
            ret += [e]
            seen.add(e)
    return ret

def ans():
    n, k = input().split(' ')
    n = int(n)
    k = int(k)
    a = input().split(' ')

    a = list(int(x) for x in a)

    if len(set(a)) > k:
        return -1

    a = uniqs(a)
    if len(a) > k:
        return -1

    a += [1]*(k - len(a))
    a = list(str(x) for x in a)

    a = a*n

    return f"{len(a)}\n{' '.join(a)}"

for t in range(T):
    print(ans())