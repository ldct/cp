#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left

### CODE HERE


# Function to find number of subarrays
# with sum exactly equal to k.
def findSubarraySum(arr, n, Sum):

    # Dictionary to store number of subarrays
    # starting from index zero having
    # particular value of sum.
    prevSum = defaultdict(lambda : 0)

    res = 0

    # Sum of elements so far.
    currsum = 0

    for i in range(0, n):

        # Add current element to sum so far.
        currsum += arr[i]

        # If currsum is equal to desired sum,
        # then a new subarray is found. So
        # increase count of subarrays.
        if currsum == Sum:
            res += 1

        # currsum exceeds given sum by currsum  - sum.
        # Find number of subarrays having
        # this sum and exclude those subarrays
        # from currsum by increasing count by
        # same amount.
        if (currsum - Sum) in prevSum:
            res += prevSum[currsum - Sum]


        # Add currsum value to count of
        # different values of sum.
        prevSum[currsum] += 1

    return res

N, K = read_int_list()
A = read_int_list()
print(findSubarraySum(A, N, K))