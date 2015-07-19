#!/usr/bin/env python3
import sys

S = input()
K = int(input())

def is_palindrome(s):
    return s == s[::-1]

def split_string(s, length):
    if len(s) == 0:
        return []
    else:
        return [s[:length]] + split_string(s[length:], length)

if len(S) % K != 0:
    print("NO")
else:
    length = int(len(S) / K)
    for substr in split_string(S, length):
        if not is_palindrome(substr):
            print("NO")
            sys.exit(0)
    print("YES")