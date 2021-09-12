#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

import random

Q = 10**5
print(Q)
curr_len = 0
for _ in range(Q):
    choices = ["1"]
    if curr_len > 10**4:
        choices += ["3"]
    if curr_len > 0:
        choices += ["2"]

    choice = random.choice(choices)

    if choice == "1":
        print(f"1 {random.randint(1, 10**9)}")
        curr_len += 1
    elif choice == "2":
        print("2")
        curr_len -= 1
    elif choice == "3":
        print("3")
    else:
        assert(False)