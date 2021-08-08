#!/usr/bin/env python3

from statistics import geometric_mean, stdev
import random, math

def random_score():
    ret = list(range(1, 8))
    random.shuffle(ret)
    return ret

def sim_once():
    return sorted([a*b*c for a,b,c in zip(random_score(), random_score(), random_score())])

def avg(lst):
    return sum(lst) / len(lst)

def order(lst):
    return (avg(lst), stdev(lst))

def median(lst):
    return sorted(lst)[len(lst)//2]

def geom(lst):
    ret = 1.0
    for e in lst: ret *= e
    return math.pow(ret, 1/len(lst))

def sim(func):
    N = 1000000
    return list(map(func, zip(*[sim_once() for _ in range(N)])))

for (a, b), c in zip(sim(order), sim(median)):
    print(f"{a} ± {b} (median {c})")