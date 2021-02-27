#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

last_dir = None

def translate(S):
    global last_dir

    dir = int(S[0]) + int(S[1])

    if dir == 0:
        assert(last_dir is not None)
        dir = last_dir
    elif dir % 2 == 1:
        dir = "left"
    else:
        dir = "right"
    last_dir = dir

    return f"{dir} {S[2:]}"

while True:
    S = input()
    if S == "99999": break
    print(translate(S))