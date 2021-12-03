#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def f():
    N, M = read_int_tuple()

    team1_score = N
    team2_score = N

    for i in range(M):
        a,b,c,d = read_int_tuple()
        team1_score -= a*b
        team2_score -= c*d

        if team1_score <= 0 and team2_score <= 0:
            return f"It's a tie at round {i+1}!"

        if team1_score <= 0:
            return f"Team 1 wins at round {i+1}!"

        if team2_score <= 0:
            return f"Team 2 wins at round {i+1}!"

    return "Oh no!"

print(f())