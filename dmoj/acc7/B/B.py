#!/usr/bin/env pypy3

import random

def fprint(*args):
	print(*args, flush=True)

N = int(input())

arr = list(range(1, N+1))

while True:
    random.shuffle(arr)
    print(*arr)
    ok = input()
    if ok == "0": break