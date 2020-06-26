#!/usr/bin/env pypy3

def ans(s):
    count = 0
    while '01' in s or '10' in s:
        if '01' in s:
            count += 1
            s = s.replace('01', '', 1)
        elif '10' in s:
            count += 1
            s = s.replace('10', '', 1)
        else:
            assert(False)
    if count % 2 == 0:
        return 'NET'
    else:
        return 'DA'
        
T = int(input())

for _ in range(T):
    s = input()
    print(ans(s))
