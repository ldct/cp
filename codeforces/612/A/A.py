#!/usr/bin/env python3

import functools

n = int(input())

def f(x):
    x = int(x)
    if x == 0: return -1
    return x % 2
ps = [f(x) for x in input().split(' ')]

total_0 = n // 2
total_1 = n - total_0

fixed_0 = len([p for p in ps if p == 0])
fixed_1 = len([p for p in ps if p == 1])

free_0 = total_0 - fixed_0
free_1 = total_1 - fixed_1

def mismatch(a, b):
    if a == -1: return 0
    if b == -1: assert(False)
    if a == b: return 0
    return 1


# interval: ps[start_idx:n]
@functools.lru_cache(maxsize=None)
def solution(free_0, free_1, last, start_idx):
    # print(f"free_0={free_0} free_1={free_1} last={last} start_idx={start_idx}")
    assert(free_0 >= 0)
    assert(free_1 >= 0)
    assert(start_idx <= n)

    if start_idx == n: return 0
    head = ps[start_idx]
    if head != -1:
        return mismatch(last, head) + solution(free_0, free_1, head, start_idx + 1)
    assert(head == -1)
    if free_0 == 0:
        return mismatch(last, 1) + solution(free_0, free_1-1, 1, start_idx + 1)
    if free_1 == 0:
        return mismatch(last, 0) + solution(free_0-1, free_1, 0, start_idx + 1)

    return min(
        mismatch(last, 1) + solution(free_0, free_1-1, 1, start_idx + 1),
        mismatch(last, 0) + solution(free_0-1, free_1, 0, start_idx + 1)
    )

    assert(False)

print(solution(free_0, free_1, -1, 0))