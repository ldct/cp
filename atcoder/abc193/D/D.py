#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from fractions import Fraction
from collections import Counter

### CODE HERE

K = read_int()
S = input()
T = input()
S = S[0:len(S)-1]
T = T[0:len(T)-1]

nums = dict()
for i in range(1, 10):
    nums[i] = K
for c in S+T:
    nums[int(c)] -= 1

def sc(nums):
    return sum([nums[k] for k in nums])

def p_draw(nums, a, b):
    nums = nums.copy()
    if nums[a] == 0: return 0
    ret = nums[a] / sc(nums)
    nums[a] -= 1
    if nums[b] == 0: return 0
    ret *= nums[b] / sc(nums)
    return ret

def score(S):
    c = Counter(S)
    ret = 0
    for i in range(1, 10):
        ret += i*(10**c[str(i)])
    return ret

ret = 0
for a in range(1, 10):
    for b in range(1, 10):
        if score(S+str(a)) > score(T+str(b)):
            ret += p_draw(nums, a, b)

print(ret)
