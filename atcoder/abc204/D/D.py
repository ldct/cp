#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def ss(target, B):
    import array
    possible = array.array('b', [1] + [0]*target)

    for b in B:
        next_possible = array.array('b', possible)
        for i in range(target):
            if possible[i] == 1 and i + b <= target:
                next_possible[i+b] = 1
        possible = next_possible

    return possible

### CODE HERE

input()
T = read_int_list()
total = sum(T)
ret = total+1
for i, e in enumerate(ss(total+1, T)):
    if e:
        ret = min(ret, max(i, total-i))

print(ret)