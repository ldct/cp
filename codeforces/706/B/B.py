#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def cdiv(x, y):
    return x // y if x % y == 0 else x // y + 1

def mex(A):
	sA = set(A)
	for i in range(0, max(A)+10):
		if i not in sA:
			return i

def ans(K, S):
    S = set(S)
    a = mex(S)
    b = max(S)
    if a == b + 1:
        return len(S) + K
    if K > 0:
        S.add(cdiv(a+b, 2))
    return len(S)

def ans_slow(K, S):
    S = set(S)
    for _ in range(K):
        a = mex(S)
        b = max(S)
        S.add(cdiv(a+b, 2))
    return len(S)

# import random
# for _ in range(10000):
#     K = random.randint(1000, 2000)
#     tc = [random.randint(1, 100) for _ in range(random.randint(1, 100))]
#     assert(ans(K, tc) == ans_slow(K, tc))

for _ in range(read_int()):
    _, K = read_int_tuple()
    S = read_int_list()
    print(ans(K, S))