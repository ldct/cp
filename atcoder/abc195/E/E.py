#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

if False:
    import random
    N = 100000
    S = ''.join(str(random.randint(0, 9)) for _ in range(N))
    X = ''.join(random.choice('AT') for _ in range(N))
else:
    N = read_int()
    S = input()[::-1]
    X = input()[::-1]

T_goal = set([0])

def inv(arr):
    return [1 - x for x in arr]

def inv(arr):
    ret = set()
    for i in range(7):
        if i not in arr:
            ret.add(i)
    return ret

for i in range(N):
    s = pow(10, i, 7)
    s *= int(S[i])
    s %= 7
    if X[i] == 'T':
        for t in set(T_goal):
            T_goal.add((t - s) % 7)
    elif X[i] == 'A':
        T_goal = inv(T_goal)
        for t in set(T_goal):
            T_goal.add((t - s) % 7)
        T_goal = inv(T_goal)
    # print(T_goal)


if 0 in T_goal:
    print('Takahashi')
else:
    print('Aoki')
