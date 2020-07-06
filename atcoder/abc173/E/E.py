#!/usr/bin/env python3

from fractions import Fraction

MODULUS = 10**9+7

def all_negative(arr):
    for _, s in arr:
        if s != -1: return False
    return True

def has_negative(arr):
    for _, s in arr:
        if s == -1: return True
    return False

def has_positive(arr):
    for _, s in arr:
        if s == 1: return True
    return False

def largest_negative(arr):
    candidates = []
    for a, s in arr:
        if s == -1: candidates += [a]
    return max(candidates)

def largest_positive(arr):
    candidates = []
    for a, s in arr:
        if s == 1: candidates += [a]
    return max(candidates)

def smallest_negative(arr):
    candidates = []
    for a, s in arr:
        if s == -1: candidates += [a]
    return min(candidates)

def smallest_positive(arr):
    candidates = []
    for a, s in arr:
        if s == 1: candidates += [a]
    return min(candidates)

def prod(arr, MODULUS=None):
    ret = 1
    for a in arr:
        ret *= a
        if MODULUS is not None:
            ret = ret % MODULUS
    return ret

def sgn(x):
    if x == 0: return 0
    if x > 0: return 1
    if x < 0: return -1
    assert(False)

N, K = input().split(' ')
K = int(K)

A = input().split(' ')
A = list(map(int, A))

def ans(A, K):

    if K == len(A):
        return prod(A, MODULUS)

    old_A = A
    A = [(abs(a), sgn(a)) for a in A]
    A = sorted(A)[::-1]

    if prod(s for (_, s) in A[0:K]) in [0, 1]:
        return prod([a for (a, _) in A[0:K]], MODULUS)

    chosen, not_chosen = A[0:K], A[K:]

    penalty_one = float("-inf")
    if has_positive(not_chosen):
        penalty_one = Fraction(largest_positive(not_chosen), smallest_negative(chosen))

    penalty_two = float("-inf")
    if has_positive(chosen) and has_negative(not_chosen):
        penalty_two = Fraction(largest_negative(not_chosen), smallest_positive(chosen))

    if penalty_one == float("-inf") and penalty_two == float("-inf"):
        if all_negative(chosen) and all_negative(not_chosen):
            A = A[::-1]
            return prod([a*s for (a, s) in A[0:K]], MODULUS)
        else:
            # print(chosen, not_chosen)
            assert(0 in old_A)
            return 0

    start = prod([a for (a, _) in chosen], MODULUS)

    penalty = max(penalty_one, penalty_two)

    start *= penalty.numerator
    start *= pow(penalty.denominator, MODULUS-2, MODULUS)

    start = ((start % MODULUS) + MODULUS) % MODULUS
    return start

# import random

# for _ in range(1000000):
#     test_case = [random.randint(-10, 10) for _ in range(5)]
#     # print(test_case)
#     ans(test_case, random.randint(0, 5))

print(ans(A, K))