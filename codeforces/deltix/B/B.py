#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

class SubstringCount:
    def __init__(self, S):
        self.count = S.count("abc")
        self.S = list(S)
    def set(self, i, c):
        for j in range(i-2, i+1):
            if j < 0: continue
            if j+2 >= len(self.S): continue
            if self.S[j] == 'a' and self.S[j+1] == 'b' and self.S[j+2] == 'c':
                self.count -= 1
        self.S[i] = c
        for j in range(i-2, i+1):
            if j < 0: continue
            if j+2 >= len(self.S): continue
            if self.S[j] == 'a' and self.S[j+1] == 'b' and self.S[j+2] == 'c':
                self.count += 1
        return self.count

N, Q = read_int_tuple()
SS = SubstringCount(input())
for _ in range(Q):
    pos, c = input().split()
    pos = int(pos)-1
    print(SS.set(pos, c))
