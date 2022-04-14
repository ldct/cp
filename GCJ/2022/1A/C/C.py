#!/usr/bin/env python3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

def distinct_permutations(iterable, r=None):
    """Yield successive distinct permutations of the elements in *iterable*.
        >>> sorted(distinct_permutations([1, 0, 1]))
        [(0, 1, 1), (1, 0, 1), (1, 1, 0)]
    Equivalent to ``set(permutations(iterable))``, except duplicates are not
    generated and thrown away. For larger input sequences this is much more
    efficient.
    Duplicate permutations arise when there are duplicated elements in the
    input iterable. The number of items returned is
    `n! / (x_1! * x_2! * ... * x_n!)`, where `n` is the total number of
    items input, and each `x_i` is the count of a distinct item in the input
    sequence.
    If *r* is given, only the *r*-length permutations are yielded.
        >>> sorted(distinct_permutations([1, 0, 1], r=2))
        [(0, 1), (1, 0), (1, 1)]
        >>> sorted(distinct_permutations(range(3), r=2))
        [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
    """
    # Algorithm: https://w.wiki/Qai
    def _full(A):
        while True:
            # Yield the permutation we have
            yield tuple(A)

            # Find the largest index i such that A[i] < A[i + 1]
            for i in range(size - 2, -1, -1):
                if A[i] < A[i + 1]:
                    break
            #  If no such index exists, this permutation is the last one
            else:
                return

            # Find the largest index j greater than j such that A[i] < A[j]
            for j in range(size - 1, i, -1):
                if A[i] < A[j]:
                    break

            # Swap the value of A[i] with that of A[j], then reverse the
            # sequence from A[i + 1] to form the new permutation
            A[i], A[j] = A[j], A[i]
            A[i + 1 :] = A[: i - size : -1]  # A[i + 1:][::-1]

    # Algorithm: modified from the above
    def _partial(A, r):
        # Split A into the first r items and the last r items
        head, tail = A[:r], A[r:]
        right_head_indexes = range(r - 1, -1, -1)
        left_tail_indexes = range(len(tail))

        while True:
            # Yield the permutation we have
            yield tuple(head)

            # Starting from the right, find the first index of the head with
            # value smaller than the maximum value of the tail - call it i.
            pivot = tail[-1]
            for i in right_head_indexes:
                if head[i] < pivot:
                    break
                pivot = head[i]
            else:
                return

            # Starting from the left, find the first value of the tail
            # with a value greater than head[i] and swap.
            for j in left_tail_indexes:
                if tail[j] > head[i]:
                    head[i], tail[j] = tail[j], head[i]
                    break
            # If we didn't find one, start from the right and find the first
            # index of the head with a value greater than head[i] and swap.
            else:
                for j in right_head_indexes:
                    if head[j] > head[i]:
                        head[i], head[j] = head[j], head[i]
                        break

            # Reverse head[i + 1:] and swap it with tail[:r - (i + 1)]
            tail += head[: i - r : -1]  # head[i + 1:][::-1]
            i += 1
            head[i:], tail[:] = tail[: r - i], tail[r - i :]

    items = sorted(iterable)

    size = len(items)
    if r is None:
        r = size

    if 0 < r <= size:
        return _full(items) if (r == size) else _partial(items, r)

    return iter(() if r else ((),))


def merge(cnt, elems):
    ret = []
    for c, e in zip(cnt, elems):
        ret += [e]*c
    return tuple(ret)

@lru_cache(None)
def load_cost(curr_stack, next_stack):
    ocs = tuple(curr_stack)
    ons = tuple(next_stack)

    if len(curr_stack) == 0:
        return len(next_stack)

    curr_stack = list(curr_stack)[::-1]
    next_stack = list(next_stack)[::-1]

    while True:
        if len(curr_stack) == 0 or len(next_stack) == 0: break
        if curr_stack[-1] == next_stack[-1]:
            curr_stack.pop()
            next_stack.pop()
        else:
            break

    return len(curr_stack) + len(next_stack)

def greedy(curr_stack, next_stack):
    ret = []

    next_stack = list(next_stack)

    for e in curr_stack:
        if e in next_stack:
            ret += [e]
            del next_stack[next_stack.index(e)]

    return tuple(ret + next_stack)

def ans_slow(W, exercises):

    exercises = [merge(e, range(W)) for e in exercises]

    @lru_cache(None)
    def dp(curr_stack, idx):
        if idx == len(exercises): return len(curr_stack)
        ret = float("inf")
        next_stack_unordered = exercises[idx]
        for next_stack in distinct_permutations(next_stack_unordered):
            ret = min(ret, load_cost(curr_stack, next_stack) + dp(next_stack, idx+1))
        return ret

    ret = dp(tuple(), 0)
    return ret

def score(lst):
    lst = lst[:] + [tuple()]
    stack = tuple()
    ret = 0
    for e in lst:
        ret += load_cost(stack, e)
        stack = e
    return ret

def ans_fast(W, exercises):

    exercises = [merge(e, range(W)) for e in exercises]

    head = exercises[0]
    tail = exercises[1:]

    ret = float("inf")

    for p in distinct_permutations(head):
        final = [p]
        for e in tail:
            final += [greedy(final[-1], e)]

        # print(p, final, score(final))
        ret = min(ret, score(final))

    return [ret]

T = int(input())
for t in range(T):
    E, W = read_int_tuple()
    exercises = [read_int_tuple() for _ in range(E)]
    print("Case #" + str(t+1) + ": " + str(ans_slow(W, exercises)) + str(ans_fast(W, exercises)))
