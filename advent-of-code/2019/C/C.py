#!/usr/bin/env pypy3

from collections import defaultdict

w1 = input().split(',')
w2 = input().split(',')

points = defaultdict(set)

def process(wire, points, marker):
    x,y = 0,0

    for instruction in wire:
        dir = instruction[0]
        num = int(instruction[1:])