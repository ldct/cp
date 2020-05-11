#!/usr/bin/env python3

T = int(input())

def ans(N, candy):
    pos = [0, N-1]
    ate = [0, 0]
    turn = 0

    last_turn_ate = 0
    this_turn_ate = 0

    moves = 0

    while pos[0] <= pos[1]:
        this_turn_ate += candy[pos[turn]]
        ate[turn] += candy[pos[turn]]
        pos[turn] += [1, -1][turn]
        if pos[0] > pos[1]: break
        if this_turn_ate > last_turn_ate:
            # print(f"{this_turn_ate}\t{last_turn_ate}\t{candy[pos[0]:pos[1]+1]}")
            turn = 1 - turn
            moves += 1
            last_turn_ate = this_turn_ate
            this_turn_ate = 0 

    return ' '.join([str(moves+1), str(ate[0]), str(ate[1])])
            


for t in range(T):
    N = int(input())
    candy = input().split(' ')
    candy = [int(x) for x in candy]

    print(ans(N, candy))