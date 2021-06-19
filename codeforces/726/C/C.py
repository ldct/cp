#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from itertools import permutations

def score(A):
    ret = 0
    for i in range(len(A)-1):
        if A[i] <= A[i+1]: ret += 1
    return ret

def ans_slow(A):
    A = sorted(A)
    md = float("inf")
    for i in range(len(A)-1):
        md = min(md, A[i+1] - A[i])

    candidates = dict()
    for p in permutations(A):
        if abs(p[0] - p[-1]) != md: continue
        candidates[score(p)] = p

    return candidates[max(candidates.keys())]

def ans(A):

    if len(A) < 5: return ans_slow(A)

    A = sorted(A)
    md = float("inf")
    for i in range(len(A)-1):
        md = min(md, A[i+1] - A[i])

    for i in range(len(A)-1):
        if A[i+1] - A[i] == md:
            A = A[i+1:] + A[0:i+1]
            return A

if False:
    print(ans_slow([3, 4, 4, 4, 5]))
elif False:
    import random
    for _ in range(10000000):
        tc = [random.randint(0, 5) for _ in range(5)]
        A = ans(tc)
        B = ans_slow(tc)

        assert(abs(A[0] - A[-1]) == abs(B[0] - B[-1]))
        if not (score(A) == score(B)):
            print(tc, A, B)
else:
    for _ in range(read_int()):
        input()
        print(*ans(read_int_list()))