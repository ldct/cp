#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())


def best(points):
    events = []
    for (start, end) in points:
        events += [start, end]

    events.sort()

    return events[len(events) // 2 - 1]

def ans(places):
    xs = []
    ys = []

    for (x1, y1, x2, y2) in places:
        xs += [(x1, x2)]
        ys += [(y1, y2)]

    return f"{best(xs)} {best(ys)}"

T = int(input())
for t in range(T):
    K = read_int()
    places = []
    for _ in range(K):
        places += [read_int_tuple()]
    print("Case #" + str(t+1) + ": " + str(ans(places)))
