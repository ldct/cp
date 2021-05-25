#!/usr/bin/env pypy3

from subprocess import run, PIPE
import random

T = 20000
X = 14600

days = []

S = ""
S += f"{T}\n"
S += f"{X}\n"
for _ in range(T//4):
    G = random.randint(5, 95)
    G = random.randint(50, 50)
    W = 10*G
    # for E in [W//10]*4:
    for E in [W, W//2, W//10, 0]:
        days += [(W, E)]
        S += f"{W} {E}\n"

p = run(['./C.py'], stdout=PIPE, input=S, encoding='ascii')

def beats(a, b):
    if a == 'R': return b == 'S'
    if a == 'P': return b == 'R'
    if a == 'S': return b == 'P'

def choose(num_R, num_P, num_S):
    if num_R + num_P + num_S == 0: return random.choice('RPS')
    return random.choices('RPS', weights=[num_S, num_R, num_P])[0]

def grade_once(W, E, strat):
    num_R = 0
    num_P = 0
    num_S = 0

    score = 0

    for c in strat:
        mine = choose(num_R, num_P, num_S)

        if mine == c: score += E
        if beats(c, mine): score += W

        if c == 'R': num_R += 1
        if c == 'P': num_P += 1
        if c == 'S': num_S += 1

    return score

def grade(W, E, strat):
    assert(len(strat) == 60)
    return grade_once(W, E, strat)

assert(0 == p.returncode)

lines = []
i = 0
total_score = 0
for line in p.stdout.split('\n')[0:T]:
    strat = line.split(": ")[1]
    W, E = days[i]
    total_score += grade(W, E, strat)
    i += 1

print(total_score/T/60)
