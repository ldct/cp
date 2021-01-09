#!/usr/bin/env pypy3

def ans(K):
    p = 7 % K
    i = 1

    for _ in range(10**6+10):
        if p == 0:
            return i

        i += 1
        p = (p*10 + 7)
        p %= K

    return -1

K = int(input())
print(ans(K))
