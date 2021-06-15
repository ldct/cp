import sys
sys.setrecursionlimit(10**6)

from functools import partial
class Infix(object):
    def __init__(self, func):
        self.func = func
    def __or__(self, other):
        return self.func(other)
    def __ror__(self, other):
        return Infix(partial(self.func, other))
    def __call__(self, v1, v2):
        return self.func(v1, v2)

import random

@Infix
def a(x, y):
    return [x, 3, y, -1]

@Infix
def o(x, y):
    return [x, 4, y, -1]

def evaluate(expr):
    if isinstance(expr, int): return expr
    if expr[3] != -1: return expr[3]
    op = expr[1]
    if op == 3: expr[3] = evaluate(expr[0]) & evaluate(expr[2])
    if op == 4: expr[3] = evaluate(expr[0]) | evaluate(expr[2])
    return expr[3]

def ans(expr):
    if isinstance(expr, int): return 1
    op = expr[1]
    a = evaluate(expr[0])
    b = evaluate(expr[2])

    if op == 3:
        if a != b: return 1
        if a == 0:
            return 1 + min(ans(expr[0]), ans(expr[2]))
        if a == 1: return min(ans(expr[0]), ans(expr[2]))

    if op == 4:
        if a != b: return 1
        if a == 0: return min(ans(expr[0]), ans(expr[2]))
        if a == 1: return 1 + min(ans(expr[0]), ans(expr[2]))




def minOperationsToFlip(expression):
    expression = expression.replace('&', ' _a_ ').replace('|', ' _o_ ').replace('_', '|')
    expr = eval(expression, globals(), locals())

    return ans(expr)

tc = '1'
for _ in range(18):
    tc = "(" + tc + ")|(" + tc + ")"

print(len(tc), minOperationsToFlip(tc))