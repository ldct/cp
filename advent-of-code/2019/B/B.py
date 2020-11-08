#!/usr/bin/env pypy3

program = list(map(int, input().split(",")))

def run_program(program):
    memory = dict()
    for i in range(len(program)):
        memory[i] = program[i]

    i = 0
    while True:
        if memory[i] == 99:
            break
        elif memory[i] == 1:
            a = memory[i+1]
            b = memory[i+2]
            c = memory[i+3]
            memory[c] = memory[a]+memory[b]
        elif memory[i] == 2:
            a = memory[i+1]
            b = memory[i+2]
            c = memory[i+3]
            memory[c] = memory[a]*memory[b]
        else:
            print("unknown opcode", i, memory[i])
            break
        i += 4

    return memory[0]

for a in range(100):
    for b in range(100):
        p = program[:]
        p[1] = a
        p[2] = b
        # print(run_program(p))
        if run_program(p) == 19690720:
            print(a,b,100*a+b)