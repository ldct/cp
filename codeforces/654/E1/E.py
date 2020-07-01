#!/usr/bin/env pypy3

n, p = input().split(' ')
N = int(n)
P = int(p)

A = input().split(' ')
A = sorted(list(map(int, A)))

from math import factorial

def factorial(n, MODULUS):
    ret = 1
    for i in range(1, n+1):
        ret = (ret*i) % MODULUS
    return ret


good_x = []

MODULUS = P

from functools import lru_cache

@lru_cache(maxsize=None)
def greater_than(candies):
    return len([a for a in A if candies >= a])

for x in range(0, 2001):
    largest_permutation = 0

    chosen = [False]*len(A)

    rank = 1
    candies = x
    while largest_permutation < len(A):
        choices = greater_than(candies)
        if choices <= largest_permutation: break
        if choices == 0: break
        rank = (rank*(choices-largest_permutation)) % MODULUS
        largest_permutation += 1
        candies += 1
        

    if largest_permutation < len(A):
        # print(f"{x} no permutations")
        pass
    elif rank % P == 0:
        # print(f"{x} rank = {rank}")
        pass
    else:
        good_x += [x]

print(len(good_x))
print(*good_x)
