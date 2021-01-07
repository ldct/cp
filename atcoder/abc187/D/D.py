#!/usr/bin/env pypy3

from sys import stdin, stdout

def input():
    return stdin.readline().strip()

def read_int_list():
	return list(map(int, input().split()))

def read_int_tuple():
	return tuple(map(int, input().split()))

def read_int():
	return int(input())

### CODE HERE

votes = []
for _ in range(read_int()):
    (a, b) = read_int_tuple()
    no_speech = -a
    speech = a + b
    votes += [(speech - no_speech, no_speech)]

votes = sorted(votes)[::-1]

score = sum(y for (x, y) in votes)

i = 0
while True:

    if i == len(votes): assert(False)
    score += votes[i][0]
    i += 1

    if score > 0:
        print(i)
        break
