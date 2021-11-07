#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def top_ans(A):
    def search(start, end, target):
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

### CODE HERE

input()
print(top_ans(read_int_list()))