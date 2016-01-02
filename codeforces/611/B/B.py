#!/usr/bin/env python3
import sys, itertools

a, b = input().split(' ')
a, b = int(a), int(b)

def exactlyOneZero():
    for totalLength in itertools.count(1):
        for leftOnes in range(1, totalLength):
            rightOnes = totalLength - leftOnes - 1

            s = "1"*leftOnes + "0" +  "1"*rightOnes
            yield int(s, 2)

def count(a, b):
    ret = 0
    for i in exactlyOneZero():
        if i < a:
            continue
        if i > b:
            return ret
        ret += 1

print(count(a, b))