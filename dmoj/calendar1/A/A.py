#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(y):
    y -= 1984
    y %= 60
    y += 60
    y %= 60
    return "甲乙丙丁戊己庚辛壬癸"[y%10] + "子丑寅卯辰巳午未申酉戌亥"[y%12]

for _ in range(read_int()):
    print(ans(read_int()))