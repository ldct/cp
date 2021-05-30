#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(T):
    if T < 34: return "Too cold, please try again."
    if T <= 35.5: return "Take a hot bath."
    if T <= 38: return "Rest if feeling unwell."
    if T <= 39: return "Take some medicine."
    if T <= 41: return "Take a cold bath and some medicine."
    if T <= 46.1: return "Go to the hospital."
    if T <= 50: return "Congrats, you have a new world record!"
    return "Too hot, please try again."

for _ in range(read_int()):
    print(ans(float(input())))