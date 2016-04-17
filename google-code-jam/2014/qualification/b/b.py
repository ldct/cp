#!/usr/bin/env python3

T = int(input(''))

def find_best_time(COST, PRODUCTION, WIN):
    def time_with_strategy(k):
        cookie_rate = 2.0
        time = 0.0
        for j in range(k):
            time += COST / cookie_rate
            cookie_rate += PRODUCTION
        return time + (WIN / cookie_rate)

    best_time = time_with_strategy(0)
    strategy_id = 1

    while True:
        next_time = time_with_strategy(strategy_id)
        if next_time > best_time:
            return best_time
        else:
            best_time = next_time
            strategy_id += 1

for i in range(T):
    parameters = input('').split(" ")
    (COST, PRODUCTION, WIN) = (float(p) for p in parameters)
    print("Case #%d: %f" % (i + 1, find_best_time(COST, PRODUCTION, WIN)))