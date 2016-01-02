#!/usr/bin/env python3
import sys

S = input()

if S == "1 of week":
    print(52)
if S == "2 of week":
    print(52)
if S == "3 of week":
    print(52)
if S == "4 of week":
    print(52)
if S == "5 of week":
    print(53)
if S == "6 of week":
    print(53)
if S == "7 of week":
    print(52)

for i in range(1, 30):
    if S == str(i) + " of month":
        print(12)

if S == "30 of month":
    print(11)
if S == "31 of month":
    print(7)