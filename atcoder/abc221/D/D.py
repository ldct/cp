#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import defaultdict

### CODE HERE

def ans(players):
    N = len(players)
    events = defaultdict(int)
    for a, b in players:
        events[a] += 1
        events[a+b] -= 1

    last_day = None
    curr_pax = 0
    prev_pax = None

    ret = defaultdict(int)

    for day in sorted(events.keys()):
        curr_pax += events[day]
        if last_day is not None:
            # print("day=", day, prev_pax, day-last_day)
            ret[prev_pax] += (day-last_day)

        last_day = day
        prev_pax = curr_pax

    r = []
    for i in range(1, N+1):
        r += [ret[i]]
    return r

players = []
for _ in range(read_int()):
    players += [read_int_tuple()]
print(*ans(players))
