#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def merge_list(left,right):
    result = list()
    i,j = 0,0
    inv_count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            inv_count += (len(left)-i)
    result += left[i:]
    result += right[j:]
    return result,inv_count


def sort_and_count(array):
    if len(array) <= 1:
        return array, 0
    middle = len(array) // 2
    left,inv_left = sort_and_count(array[:middle])
    right,inv_right = sort_and_count(array[middle:])
    merged, count = merge_list(left,right)
    count += (inv_left + inv_right)
    return merged, count


def count_inversions(arr):
    _, ret = sort_and_count(arr[:])
    return ret

### CODE HERE

MODULUS = 10**9+7

def ans(A, K):
    ret = count_inversions(A)
    ret *= K
    ret %= MODULUS

    freq = [0]*2009

    for a in A:
        freq[a] += 1

    for i in range(len(freq)-2, -1, -1):
        freq[i] += freq[i+1]

    for a in A:
        ret += freq[a+1]*K*(K-1)//2
        ret %= MODULUS

    return ret

N, K = read_int_tuple()
A = read_int_list()

print(ans(A, K))