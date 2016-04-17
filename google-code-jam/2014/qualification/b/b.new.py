#!/usr/bin/env python3

T = int(input(''))

def find_best_time(COST, PRODUCTION, WIN):
    memo = {}
    def time_with_strategy(k):
        if (k in memo):
            return memo[k]
        cookie_rate = 2.0
        time = 0.0
        for j in range(k):
            time += COST / cookie_rate
            cookie_rate += PRODUCTION
        memo[k] = time + (WIN / cookie_rate)
        return memo[k]

    max_id = int(WIN / PRODUCTION) + 2

    def bs(low, high):
        if low == high:
            return low
        elif low + 1 == high:
            if time_with_strategy(low) > time_with_strategy(high):
                return time_with_strategy(high)
            else:
                return time_with_strategy(low)
        else:
            mid = int((low + high) / 2)
            if time_with_strategy(mid) > time_with_strategy(low):
                return bs(low, mid)
            else:
                return bs(mid, high)
    return bs(0, max_id)
for i in range(T):
    parameters = input('').split(" ")
    (COST, PRODUCTION, WIN) = (float(p) for p in parameters)
    print("Case #%d: %f" % (i + 1, find_best_time(COST, PRODUCTION, WIN)))