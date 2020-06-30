#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

def run_program(n, program):
    for op, a in program:
        assert(op in "&|^")
        if op == '&': n = n & a
        if op == '|': n = n | a
        if op == '^': n = n ^ a
    return n

N = int(input())

q = 1023
r = 0

original_program = []
for _ in range(N):
    op, s = input().split(' ')
    s = int(s)

    original_program += [(op, s)]

    if op == '&':
        q = q & s
        r = r & s
    elif op == '^':
        r = r ^ s
    elif op == '|':
        q, r = (q ^ (q&s)), (r ^ s ^ (r&s))
    else:
        assert(False)

final_program = [('&', q), ('^', r)]

print(2)
print(f"& {q}")
print(f"^ {r}")