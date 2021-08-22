#!/usr/bin/env python3

from sys import stdin, stdout, setrecursionlimit

from functools import lru_cache

setrecursionlimit(10000)

def nc(num):

    num = "1" + num

    @lru_cache(None)
    def int_of(i, j):
        return int(num[i:j])

    @lru_cache(None)
    def comp(i, j, k):
        return True
        return int_of(i, j) <= int_of(j, k)

    @lru_cache(None)
    def ans_sum(i, j):
        ret = 0
        if j == len(num):
            return ans(i, j)
        if j > len(num): return 0

        return (ans(i, j) + ans_sum(i, j+1)) % (10**9+7)

    @lru_cache(None)
    def ans(i, j):
        ret = 0
        if j == len(num): return 1
        if num[j] == "0": return 0
        k = 2*j - i
        if k <= len(num):
            if comp(i, j, k):
                ret += ans(j, k)
        ret += ans_sum(j, k+1)
        ret %= (10**9+7)

        return ret

    return ans(0, 1)

print(nc("9"*3000))