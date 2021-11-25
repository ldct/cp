#!/usr/bin/env pypy3

### Statement

"""
You have an array of length n that are initially zero. In each step, you may choose a consecutive interval [L, R] and increase the values by 1. Find the minimum number of operations required so that the i-th entry of the array is equal to d_i.

https://dmoj.ca/problem/noip18p1
"""

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def top_ans(A):
    def search(start, end, target):
        # print("search", A[start:end], target)
        for i in range(start, end):
            if A[i] == target:
                return i
        return None
    def min_range(start, end):
        return min(A[start:end])

    def ans(i, j, sub):
        if i >= j: return 0
        k = search(i, j, sub)
        if k is not None:
            ret = ans(i, k, sub) + ans(k+1, j, sub)
            return ret
        m = min_range(i, j)
        assert(m - sub >= 0)
        ret = m - sub + ans(i, j, m)
        return ret
    return ans(0, len(A), 0)

def ans_fast(A):
    # https://wyy603.github.io/2019/01/22/NOIP2018-%E6%8F%90%E9%AB%98%E7%BB%84-%E9%A2%98%E8%A7%A3/
    N = len(A)
    lastd = 0

    d_arr = []

    for d in A:
        d_arr += [d - lastd]
        lastd = d

    d_arr += [-lastd]

    assert(sum(d_arr) == 0)
    return sum([d for d in d_arr if d > 0])

### CODE HERE

input()
tc = read_int_list()
ans = ans_fast(tc)
assert(ans == top_ans(tc))
print("ans=", ans)