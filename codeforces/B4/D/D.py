#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left

### CODE HERE

def lis(sequence):
    """Finds the longest increasing subsequence in sequence using dynamic
    programming.  This solution is O(n^2)."""

    longest_subsequence_ending_with = []
    backreference_for_subsequence_ending_with = []
    current_best_end = 0

    for curr_elem in range(len(sequence)):
        # It's always possible to have a subsequence of length 1.
        longest_subsequence_ending_with.append(1)

        # If a subsequence is length 1, it doesn't have a backreference.
        backreference_for_subsequence_ending_with.append(None)

        for prev_elem in range(curr_elem):
            subsequence_length_through_prev = (longest_subsequence_ending_with[prev_elem] + 1)

            # If the prev_elem is smaller than the current elem (so it's increasing)
            # And if the longest subsequence from prev_elem would yield a better
            # subsequence for curr_elem.
            if ((sequence[prev_elem] < sequence[curr_elem]) and
                    (subsequence_length_through_prev >
                         longest_subsequence_ending_with[curr_elem])):

                # Set the candidate best subsequence at curr_elem to go through prev.
                longest_subsequence_ending_with[curr_elem] = (subsequence_length_through_prev)
                backreference_for_subsequence_ending_with[curr_elem] = prev_elem
                # If the new end is the best, update the best.

        if (longest_subsequence_ending_with[curr_elem] >
                longest_subsequence_ending_with[current_best_end]):
            current_best_end = curr_elem

    # Output the overall best by following the backreferences.

    ret = []
    for j in range(len(sequence)):
        best_subsequence = []
        current_backreference = j

        while current_backreference is not None:
            best_subsequence.append(sequence[current_backreference])
            current_backreference = (backreference_for_subsequence_ending_with[current_backreference])

        best_subsequence.reverse()

        ret += [best_subsequence]

    return ret

N, W, H = read_int_tuple()
index_of = dict()
envelopes = []
for i in range(N):
    w, h = read_int_tuple()
    index_of[(w,h)] = i
    envelopes += [(w, -h)]

index_of[(W, H)] = N
envelopes += [(W, -H)]
envelopes = sorted(set(envelopes))
envelopes = [(w, -h) for (w, h) in envelopes]
eh = [(h, i) for (i, (w, h)) in enumerate(envelopes)]

print(eh)

best = 0
arg = None

for l in lis(eh):
    lll = [envelopes[i] for (_, i) in l]
    print(lll)
    if (W, H) in lll:
        ll = l[1 + lll.index((W, H)):]
        if len(ll) > best:
            best = len(ll)
            arg = ll

if arg is None:
    print(0)
else:
    print(best)
    print(" ".join(str(1 + index_of[s]) for s in ll))