#!/usr/bin/env python3

def ans(S):
    if len(S) < 4: return "NO"
    if S.startswith("2020") and S.endswith(""): return "YES"
    if S.startswith("202") and S.endswith("0"): return "YES"
    if S.startswith("20") and S.endswith("20"): return "YES"
    if S.startswith("2") and S.endswith("020"): return "YES"
    if S.startswith("") and S.endswith("2020"): return "YES"
    return "NO"

for _ in range(int(input())):
    input()
    S = input()
    print(ans(S))
