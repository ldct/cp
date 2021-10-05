#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import chain, combinations, permutations

def subsets(iterable, low=0, high=None):
    "subsets([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    if high is None:
        high = len(s)
    return chain.from_iterable(combinations(s, r) for r in range(low, high+1))

### CODE HERE

def ans_slow(X, A):
    def ok(swaps, A, B=None):

        if B is None:
            B = len(A)*len(A)
        if A == sorted(A): return True
        if B <= 0: return False

        for i,j in swaps:
            new_A = A[:]
            new_A[i], new_A[j] = new_A[j], new_A[i]

            if ok(swaps, new_A, B-1): return True

        return False

    pairs = []
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if abs(i-j) >= X:
                pairs += [(i, j)]

    if ok(pairs, A): return "YES"
    return "NO"

def ans(X, A):
    fixed = []
    left = []
    right = []
    for i in range(len(A)):
        if i + X >= len(A) and i - X < 0:
            # print(f"{i} is fixed")
            fixed += [A[i]]
        else:
            if i < len(A) / 2:
                left += [A[i]]
            else:
                right += [A[i]]

    # print(left, fixed, right)

    if len(fixed) == 0: return "YES"
    if fixed != sorted(fixed): return "NO"

    assert(len(left) == len(right))

    if len(left) == 0:
        if fixed == sorted(fixed): return "YES"
        if fixed != sorted(fixed): return "NO"

    K = len(left)
    sides = left + right
    sides.sort()

    left = sides[0:K]
    right = sides[K:]
    if (max(left) <= min(fixed) <= max(fixed) <= min(right)): return "YES"

    return "NO"

if False:
    print(ans(3, [97, 35, 48, 11]))
    print(ans_slow(3, [97, 35, 48, 11]))
elif False:
    import random
    for _ in range(10000):
        N = 4
        X = random.randint(1, N)
        A = [random.randint(0, 100) for _ in range(N)]
        print(X, A)
        assert(ans(X, A) == ans_slow(X, A))
else:
    for _ in range(read_int()):
        N, X = read_int_tuple()
        A = read_int_list()
        print(ans(X, A))