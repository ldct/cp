#!/usr/bin/env python3

T = int(input())

def cost_01(N, prefix_0, prefix_1, suffix_0, suffix_1):
    ans = float("inf")
    for i in range(N+1):
        if i > 0:
            front_cost = prefix_1[i-1]
        else:
            front_cost = 0
        if i < N:
            back_cost = suffix_0[i]
        else:
            back_cost = 0

        ans = min(ans, front_cost + back_cost)
    return ans

def cost_10(N, prefix_0, prefix_1, suffix_0, suffix_1):
    ans = float("inf")
    for i in range(N+1):
        if i > 0:
            front_cost = prefix_0[i-1]
        else:
            front_cost = 0
        if i < N:
            back_cost = suffix_1[i]
        else:
            back_cost = 0

        ans = min(ans, front_cost + back_cost)
    return ans

def ans(s):
    if not ("01" in s and "10" in s):
        return 0

    N = len(s)
    
    if s[0] == "0":
        prefix_0 = [1]
        prefix_1 = [0]
    else:
        prefix_0 = [0]
        prefix_1 = [1]

    for i in s[1:]:
        if i == "0":
            prefix_0 += [prefix_0[-1] + 1]
            prefix_1 += [prefix_1[-1] + 0]
        else:
            prefix_0 += [prefix_0[-1] + 0]
            prefix_1 += [prefix_1[-1] + 1]

    s = s[::-1]

    if s[0] == "0":
        suffix_0 = [1]
        suffix_1 = [0]
    else:
        suffix_0 = [0]
        suffix_1 = [1]

    for i in s[1:]:
        if i == "0":
            suffix_0 += [suffix_0[-1] + 1]
            suffix_1 += [suffix_1[-1] + 0]
        else:
            suffix_0 += [suffix_0[-1] + 0]
            suffix_1 += [suffix_1[-1] + 1]

    s = s[::-1]
    suffix_0 = suffix_0[::-1]
    suffix_1 = suffix_1[::-1]

    return min(
        cost_01(N, prefix_0, prefix_1, suffix_0, suffix_1),
        cost_10(N, prefix_0, prefix_1, suffix_0, suffix_1)
    )


for t in range(T):
    s = input()
    print(ans(s))