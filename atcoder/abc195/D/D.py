#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

N, M, Q = read_int_tuple()

luggages = []

for _ in range(N):
    w, v = read_int_tuple()
    luggages += [(v, w)]

luggages = sorted(luggages)[::-1]

boxes = read_int_tuple()

def ans(boxes, luggages):
    boxes = sorted(boxes)
    ret = 0
    for v, w in luggages:
        for i in range(len(boxes)):
            if boxes[i] >= w:
                ret += v
                del boxes[i]
                break
    return ret

for _ in range(Q):
    L, R = read_int_tuple()
    L -= 1
    R -= 1
    new_boxes = boxes[0:L] + boxes[R+1:]
    print(ans(new_boxes, luggages))