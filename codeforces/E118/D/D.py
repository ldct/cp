#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

MODULUS = 998244353

from itertools import chain, combinations, product

def subsets(iterable, low=0, high=None):
    "subsets([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    if high is None:
        high = len(s)
    return chain.from_iterable(combinations(s, r) for r in range(low, high+1))

### CODE HERE

def mex(A):
    sA = set(A)
    for i in range(0, 200):
        if i not in sA: return i
    assert(False)

def correct(seq):
    for i in range(len(seq)):
        if not (1 >= abs(seq[i] - mex(seq[0:i+1]))):
            return False
    return True


def subsequences(S):
    ret = []
    for indices in subsets(range(len(S))):
        ret += [[S[i] for i in indices]]
    return ret

from functools import lru_cache

def ans_bottom(S):
    i = len(S)
    sz = len(S)+9
    dp1 = [1]*(sz)
    dp2 = [1]*(sz)
    while i > 0:
        i -= 1
        dp1_add = dict()
        dp2_add = dict()

        if S[i]+1 < sz: dp1_add[S[i]+1] = dp1[S[i]+1]
        dp1_add[S[i]-1] = dp1[S[i]-1]

        if S[i]+1 < sz: dp2_add[S[i]+1] = dp2[S[i]+1]
        if S[i]+1 < sz: dp2_add[S[i]] = dp2[S[i]+1]
        dp2_add[S[i]-1] = dp1[S[i]-1]

        for k in dp1_add:
            dp1[k] += dp1_add[k]
            dp1[k] %= MODULUS
        for k in dp2_add:
            dp2[k] += dp2_add[k]
            dp2[k] %= MODULUS
    return (dp2[0]-1) % MODULUS

def ans(S):
    @lru_cache(None)
    def dp(mex_before, has_top, i):
        if i == len(S): return 1
        if has_top:
            ret = dp(mex_before, True, i+1)
            if S[i] in [mex_before-1, mex_before+1]: ret += dp(mex_before, True, i+1)
            return ret % MODULUS
        else:
            ret = dp(mex_before, False, i+1)
            if S[i]+1 == mex_before: ret += dp(mex_before, False, i+1)
            if S[i] == mex_before: ret += dp(mex_before+1, False, i+1)
            if S[i]-1 == mex_before: ret += dp(mex_before, True, i+1)
            return ret % MODULUS
    return (dp(0, False, 0)-1) % MODULUS

def ans_slow(S):
    ret = 0
    for s in subsequences(S):
        if len(s) > 0 and correct(s):
            ret += 1
    return ret

if False:
    import random
    tc = [0 for _ in range(1000)]
    print(ans(tc))
elif False:
    for N in range(10):
        for p in product(range(10), repeat=N):
            assert(ans(p) == ans_bottom(p))
        print("checked", N)
elif True:
    for _ in range(read_int()):
        input()
        tc = read_int_list()
        print(ans_bottom(tc))
        # assert(ans(tc) == ans_slow(tc))

# seq = [0]*5
# import itertools
# for N in range(5):
#     for p in itertools.product(range(N+3), repeat=N):
#         if correct(p):
#             print(p)
#             seq[len(p)] += 1
# print(seq)