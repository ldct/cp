#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def subset_sums(arr, i, UB):
    if i == len(arr):
        return [0]
    ret = subset_sums(arr, i+1, UB)
    c = [r + arr[i] for r in ret]
    return [r for r in ret + c if r <= UB]

### CODE HERE

def possible_slow(N):
    total = N*(N+1)//2
    if total % 2 == 1: return False
    return total//2 in subset_sums(list(range(1, N+1)), 0, float("inf"))

def pairs(arr):
    N = len(arr) // 2
    ret = []
    for i in range(N):
        a, b = arr[2*i], arr[2*i+1]
        ret += [(a, b)]
    return ret

def clean(arr):
    return [a for a in arr if a > 0]

def possible(N):
    if (N*(N+1)//2) % 2 == 1: return False
    objects = list(range(1, N+1))

    if len(objects) % 2 == 1:
        objects = [0] + objects

    objects = pairs(objects)
    left = []
    right = []
    for i, (a, b) in enumerate(objects):
        if i % 2 == 0:
            left += [a]
            right += [b]
        else:
            right += [a]
            left += [b]

    assert(len(left) == len(right))

    return clean(left), clean(right)

def drop(arr):
    print(len(arr))
    print(*arr)

r = possible(read_int())
if r == False:
    print("NO")
else:
    print("YES")
    a, b = r
    drop(a)
    drop(b)