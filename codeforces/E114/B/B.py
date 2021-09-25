#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def num_adj(str):
    ret = 0
    for i in range(len(str)-1):
        if str[i] == str[i+1]:
            ret += 1
    return ret

def find_minm_slow(a, b, c):
    ret = float("inf")
    from itertools import permutations
    for str in permutations("a"*a + "b"*b + "c"*c):
        ret = min(ret, num_adj(str))
    return ret

def find_minm(a, b, c):
    [a, b, c] = sorted([a, b, c])[::-1]

    if a == (b + c):
        return 0
    if a > (b + c):
        return a - (b + c) - 1
    return 0

def ans_slow(a, b, c, m):
    from itertools import permutations
    for str in permutations("a"*a + "b"*b + "c"*c):
        if m == num_adj(str): return True
    return False

def ans(a, b, c, m):
    MIN_M = find_minm(a, b, c)
    MAX_M = a+b+c - 3
    if not (MIN_M <= m <= MAX_M): return False
    return True

if True:
    for _ in range(read_int()):
        print("Yes" if ans(*read_int_tuple()) else "No")
else:
    for a in range(1, 5):
        for b in range(1, 5):
            for c in range(1, 5):
                for m in range(1, 5):
                    # print(a, b, c, m)
                    assert(ans(a, b, c, m) == ans_slow(a, b, c, m))