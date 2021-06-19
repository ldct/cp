#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(S, K):
    def seed(s, k):
        ret = ""
        while len(ret) < k:
            ret += s
        return ret[0:k]

    prefixes = [seed(S[0:i], K) for i in range(1, len(S)+1)]

    def ans2(s, k):
        if k == 0: return ""
        return min(prefixes[0:k])[0:k]

    return ans2(S, K)

N, K = read_int_tuple()
S = input()
print(ans(S, K))