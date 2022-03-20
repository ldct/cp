#!/usr/bin/env pypy3

from sys import stdin, stdout
from itertools import product, combinations_with_replacement
from math import factorial

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def interesting(seq):
    if sum(seq) == 0: return False
    A = 1
    for c in seq:
        A *= c
    return (A % sum(seq)) == 0

interesting_sorted = list(combinations_with_replacement(range(10), 12))
interesting_sorted = [seq for seq in interesting_sorted if interesting(seq)]

MAX_CHAR = 10
MAX_FACT = 20
fact = [None] * (MAX_FACT)

def precomputeFactorials():
    fact[0] = 1
    for i in range(1, MAX_FACT):
        fact[i] = fact[i - 1] * i

# Function for nth permutation
def nPermute(string, n):
    n += 1

    precomputeFactorials()

    # length of given string
    length = len(string)

    # Count frequencies of all
    # characters
    freq = [0] * (MAX_CHAR)
    for i in range(0, length):
        freq[string[i]] += 1

    # out string for output string
    out = [None] * (MAX_CHAR)

    # iterate till sum equals n
    Sum, k = 0, 0

    # We update both n and sum in
    # this loop.
    while Sum != n:

        Sum = 0

        # check for characters present in freq[]
        for i in range(0, MAX_CHAR):
            if freq[i] == 0:
                continue

            # Remove character
            freq[i] -= 1

            # calculate sum after fixing
            # a particular char
            xsum = fact[length - 1 - k]
            for j in range(0, MAX_CHAR):
                xsum = xsum // fact[freq[j]]
            Sum += xsum

            # if sum > n fix that char as
            # present char and update sum
            # and required nth after fixing
            # char at that position
            if Sum >= n:
                out[k] = i
                n -= Sum - xsum
                k += 1
                break

            # if sum < n, add character back
            if Sum < n:
                freq[i] += 1

    # if sum == n means this char will provide
    # its greatest permutation as nth permutation
    i = MAX_CHAR-1
    while k < length and i >= 0:
        if freq[i]:
            out[k] = i
            freq[i] -= 1
            i += 1
            k += 1

        i -= 1

    # print result
    return out[:k]


print(nPermute(list(range(10)), 100000))