#!/usr/bin/env pypy3

def prod(arr):
    ret = 1
    for a in arr:
        ret *= a
    return ret


def smallestPow(k):
    for i in range(1, 100000):
        if i**10 > k: return i-1

def ans(K):
    s = smallestPow(K)

    ret = [s]*10

    while prod(ret) < K:
        ret[ret.index(min(ret))] += 1

    retStr = ""

    for i in range(10):
        retStr += "codeforces"[i]*ret[i]

    return retStr

K = int(input())

print(ans(K))