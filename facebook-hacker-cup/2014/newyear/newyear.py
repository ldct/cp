#!/usr/bin/env python3

from itertools import chain, combinations
import sys

sys.setrecursionlimit(2000)

#itertools recipe
def powerset(iterable):
  xs = list(iterable)
  return chain.from_iterable( combinations(xs,n) for n in range(len(xs)+1) )

def get_ints():
    return map(int, input('').split(' '))

def summable_slow(goal_p, goal_f, goal_c, foods):
    for subset in powerset(foods):
        if (goal_p, goal_f, goal_c) == tuple(map(sum, list(zip(*subset)))):
            return True
    return False

def summable(goal_p, goal_f, goal_c, foods, N, memo):

    # is goal reachable with foods[N:]

    if (goal_p, goal_f, goal_c) == (0, 0, 0):
        return True
    if goal_p < 0:
        return False
    if goal_c < 0:
        return False
    if goal_f < 0:
        return False

    if (goal_p, goal_f, goal_c, N) in memo:
        return memo[goal_p, goal_f, goal_c, N]

    if N == len(foods):
        return False

    if summable(goal_p, goal_f, goal_c, foods, N + 1, memo):
        memo[(goal_p, goal_f, goal_c, N)] = True
        return True

    (food_p, food_f, food_c) = foods[N]
    if summable(goal_p - food_p, goal_f - food_f, goal_c - food_c, foods, N + 1, memo):
        memo[(goal_p, goal_f, goal_c, N)] = True
        return True

    memo[(goal_p, goal_f, goal_c, N)] = False
    return False

(T, ) = get_ints()
for t in range(T):
    (goal_p, goal_f, goal_c ) = get_ints()
    (N, ) = get_ints()

    foods = []
    for i in range(N):
        (food_p, food_f, food_c) = get_ints()
        foods += [(food_p, food_f, food_c)]

    yn = 'yes' if summable(goal_p, goal_f, goal_c, foods, 0, {}) else 'no'    
    print("Case #%d: %s" % (t + 1, yn))