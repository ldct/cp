#!/usr/bin/env pypy3

from sys import stdin, stdout

def input():
    return stdin.readline().strip()

from collections import defaultdict

def back_of(gangs):
    for i in range(len(gangs)):
        if gangs[i] != gangs[0]:
            return i

def ans(gangs):
    if len(set(gangs)) == 1:
        print("NO")
        return

    gs = set()

    for i in range(len(gangs)):
        gs.add(gangs[i])

    print("YES")
    for i in range(len(gangs)):
        if gangs[i] != gangs[0]:
            print(1, i+1)

    back = back_of(gangs)

    for i in range(1, len(gangs)):
        if gangs[i] == gangs[0]:
            print(back+1, i+1)



for _ in range(int(input())):
    input()
    gangs = list(map(int, input().split()))
    ans(gangs)