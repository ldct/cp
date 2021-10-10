#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ok(day1, day2, preferences):
    N = len(preferences)
    num_day1_only = 0
    num_day2_only = 0
    num_both = 0

    for arr in preferences:
        if arr[day1] == 1 and arr[day2] == 1:
            num_both += 1
        elif arr[day1] == 1:
            num_day1_only += 1
        elif arr[day2] == 1:
            num_day2_only += 1
        else:
            return False

    if num_day1_only > N//2: return False
    if num_day2_only > N//2: return False
    return True


def ans(preferences):
    for day1 in range(5):
        for day2 in range(day1+1, 5):
            if ok(day1, day2, preferences):
                return "YES"
    return "NO"

for _ in range(read_int()):
    N = read_int()
    preferences = []
    for _ in range(N):
        preferences += [read_int_list()]
    print(ans(preferences))
