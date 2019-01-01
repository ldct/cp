#!/usr/bin/env python3

with open('./input.txt') as f:
    print(sum(int(line) for line in f.readlines()))